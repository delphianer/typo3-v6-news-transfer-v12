import json
import os


def pw_data():
    pwd_file_name = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config'),'pwd.json')
    if os.path.exists(pwd_file_name):
        with open(pwd_file_name, 'r') as f:
            data = json.load(f)
    else:
        data = {"uid" : "admin", "pwd":"G8Tqn2f"}
        with open(pwd_file_name, 'w') as f:
            json.dump(data, f)
    return data

def load_config():
    config_file_name = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config'),'config.json')
    if os.path.exists(config_file_name):
        with open(config_file_name, 'r') as f:
            config_data = json.load(f)
    else:
        config_data = {
            "init_website" : "http://www.drk-etzenrot.de/typo3/",
            "pwd_user_field" : '//*[@id="t3-username"]',
            "pwd_password_field" : '//*[@id="t3-password"]',
            "wait_after_click" : 5,
            "click_events_to_go_to_news" : {
                "nachrichten_ansicht" : 'Nachrichten'#'//*[@id="web_txttnewsM1"]/a/span[2]'
                #,"news_storage" : '//*[@id="ext-gen137"]'
                ,"news_storage" : 'News Storage' #'//*[@id="ext-gen139"]'
            }
            , "select_first_news_selectorx": '/html/body/div[1]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[4]/a'
            , "select_first_news_selectory": '/html/body/div[1]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[4]/a'
            , "news_selector_prefix":        '//*[@id="ttnewslist"]/table/tbody/tr['
            , "news_selector_start_number" : 2
            , "news_selector_end_number" : 16
            , "news_selector_last_page_end_number" : 9
            , "news_selector_postfix": ']/td[4]'
            , "close_news_selector" : '//*[@id="typo3-docheader"]/div[2]/div[1]/div[1]/a/span'
            , "fields_for_download" : {
                "titel" : '//*[@name="data[tt_news][128][title]_hr"]'
                #,"untertitel": '//*[@id="tceforms-textfield-66282233ab927013226923"]//div'
            }
            , "next_page_selector" : '//*[@id="ttnewslist"]/table/tbody/tr[16]/td[4]/a'
            , "pages_count" : 8
            , "log_off_selector" : '//*[@id="logout-submit-button"]'
        }
        #with open(config_file_name, 'w') as f:
        #    json.dump(config_data, f)
    return config_data
