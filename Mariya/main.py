#coding=1251
from selenium import webdriver
from time import sleep
import os
from selenium import webdriver

homeDir = os.getcwd()
loadsDir = homeDir + '\\data\\loads'

def auto_page_pass(inn):
    chrome_options = webdriver.ChromeOptions()
    '''
    ������� ��� ���������� ���������.
    '''
    chromedriver = homeDir + "\\sourses\\chromedriver.exe"      
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": loadsDir,                  
             "directory_upgrade": True}                     
    #homedir - �������� ���������� �� 
    chrome_options.add_experimental_option('prefs', prefs)
    
    #"--disable-extensions"
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    browser.get('https://websbor.gks.ru/online/info')
    sleep(3)
    #��� ������ �������� � ������� ������������ XPath (F12 � ��������, ����� ������� ��������, ��� - Copy - XPath)
    # ������ � ���� "������� � email" 123
    browser.find_element("xpath",'//*[@id="inn"]').send_keys(inn)
    sleep(1)
    #������� ������ 1
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[1]').click()
    sleep(1)
    browser.quit()
    return 0
#auto_page_pass()






if __name__ == '__main__':
    
    pass