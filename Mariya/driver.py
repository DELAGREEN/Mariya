from selenium import webdriver
from time import sleep
from selenium import webdriver
from config import (path_to_home_dir, path_to_loads_dir, time_sleep)


def auto_page_pass(inn):
 chrome_options = webdriver.ChromeOptions()
 '''
 Драйвер для управления браузером.
 '''
 chromedriver = path_to_home_dir + "\\sourses\\chromedriver.exe"      
 prefs =  {"profile.default_content_settings.popups": 0,
          "download.default_directory": path_to_loads_dir,                  
          "directory_upgrade": True}                      
 chrome_options.add_experimental_option('prefs', prefs)
 #"--disable-extensions"
 browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
 browser.get('https://websbor.gks.ru/online/info')
 sleep(time_sleep)
 #для поиска элемента в примере используется XPath (F12 в браузере, поиск нужного элемента, ПКМ - Copy - XPath)
 # ввести в поле "Телефон и email" 123
 print(f'Open is {inn}')
 browser.find_element("xpath",'//*[@id="inn"]').send_keys(inn)
 sleep(time_sleep)
 #нажатие кнопки 1
 browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
 sleep(time_sleep)
 browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
 sleep(time_sleep)
 browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[3]').click()
 sleep(time_sleep)    
#auto_page_pass()