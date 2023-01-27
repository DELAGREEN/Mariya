#coding=1251
from ssl import Options
from bs4 import BeautifulSoup
from selenium import webdriver
##from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
import os
#import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#dataList = data.dataList
data_list = '2130224767'
homeDir = os.getcwd()
#inn_data = '1254'

def auto_page_pass(inn_data):
    chrome_options = Options()
    '''
    Драйвер для управления браузером.
    '''
    chromedriver = homeDir + "\\sourses\\chromedriver.exe"      
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": homeDir + "\data",                  
             "directory_upgrade": True}                     
    #homedir - домашняя директория ку 
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    browser.get('https://websbor.gks.ru/online/info')
    sleep(5)
    #для поиска элемента в примере используется XPath (F12 в браузере, поиск нужного элемента, ПКМ - Copy - XPath)
    # ввести в поле "Телефон и email" 123
    browser.find_element("xpath",'//*[@id="inn"]').send_keys(inn_data)
    sleep(1)
    #нажатие кнопки 1
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[1]').click()
    sleep(3)
    browser.quit()
    return 0


if __name__ == '__main__':
    pass