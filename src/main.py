import time

from selenium.webdriver.common.by import By

from common import F
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.first_run import load_config, pw_data

# # # # # # #
# Main Part #
# # # # # # #
if __name__ == "__main__":
    conf = load_config()
    pwd = pw_data()

    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1900x1200")  # todo: in Config rein ...
    driver = webdriver.Chrome(options=options)
    driver.get(conf.get("init_website"))

    username_field = driver.find_element(By.XPATH, conf.get("pwd_user_field"))
    username_field.send_keys(pwd.get("uid"))
    pwd_field = driver.find_element(By.XPATH, conf.get("pwd_password_field"))
    pwd_field.send_keys(pwd.get("pwd"))
    pwd_field.send_keys(Keys.RETURN)

    time.sleep(conf.get("wait_after_click"))

    for key in conf.get("click_events_to_go_to_news"):
        print("Klicke auf", key)
        selektor = driver.find_element(By.LINK_TEXT, conf.get("click_events_to_go_to_news").get(key))
        selektor.click()
        time.sleep(conf.get("wait_after_click"))

    for page in range(1, conf.get("pages_count")):
        if page == conf.get("pages_count"):
            number_of_news = conf.get("news_selector_last_page_end_number")
        else:
            number_of_news = conf.get("news_selector_end_number")
        for news_entry in range(conf.get("news_selector_start_number"), number_of_news):
            news_entry_selector = conf.get("news_selector_prefix") + str(news_entry) + conf.get("news_selector_postfix")
            print("News nummer: ", str(page), "->", str(news_entry), ") news_entry_selector", news_entry_selector)
            selektor = driver.find_element(By.XPATH, news_entry_selector)
            print("tag_name gefunden: ",selektor.tag_name)
            print("Text gefunden: ", selektor.text)
        time.sleep(conf.get("wait_after_click"))
    #open_news = driver.find_element(By.XPATH, conf.get("select_first_news_selector"))
    #open_news.click()

    # Titel: //*[@id="tceforms-textfield-6626d10e995e5086748469"]
    #        name=data[tt_news][128][title]_hr
    #
    # Titel auslesen mit dem name-attribut:
    if driver is None: # Block "auskommentiert"
        for key in conf.get("fields_for_download"):
            field = driver.find_element(By.XPATH, conf.get("fields_for_download").get(key))
            field_text = field.text
            print(key, "->field_text:", field_text)
            # todo: weitere felder auslesen

        # News schließen:
        close_news = driver.find_element(By.XPATH, conf.get("close_news_selector"))
        close_news.click()
    # Bilder-Auswahl: //*[@id="tceforms-multiselect-6626d10ee5988167940643"]
    # noch etwas: //*[@id="tceforms-multiselect-6626d10ee5988167940643"]/option

    # //*[@id="typo3-inner-docbody"]/form/table/tbody/tr[5]/td[2]/a
    # //*[@id="typo3-inner-docbody"]/form/table/tbody/tr[6]/td[2]/a

    # Finde das erste Bild auf der Ergebnisseite
    # img_element = driver.find_element_by_css_selector("div.thumb.tright > div > a > img")
    # img_src = img_element.get_attribute("src")

    # Lade das Bild herunter
    # img_name = "pferd.jpg"
    # with open(img_name, "wb") as f:
    #    f.write(driver.get(img_src).content)

    # print(f"Das Bild '{img_name}' wurde erfolgreich heruntergeladen.")

    time.sleep(conf.get("wait_after_click"))

    # abmelden:
    logout_field = driver.find_element(By.XPATH, conf.get("log_off_selector"))
    logout_field.click()

    time.sleep(conf.get("wait_after_click"))

    # Schließe den Browser
    driver.quit()
