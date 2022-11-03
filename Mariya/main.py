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

#������ ���� ������ ��� �������� ������� ���� �����
#� ��������� �� ����������� ���������� � ������� ������� ��������� �����

##chromeOptions = webdriver.ChromeOptions()

#!!!!!!!!!!!!!!���� --- ��� ��������� �� ����� ������ ��� ��� ���� ��������� 
#���������� ����� ���������� �� Path � ����� ��� ��� ��� ����� ����������
#######prefs = {"download.default_directory" : "C:\\Users\\igorm\\Downloads\\test"}
#######
#######chromeOptions.add_experimental_option("prefs",prefs)
#######
########��������!!!!!!!!!!!!!!!!!!!!�� ������ ������� ��������� webdriver
#######chromedriver = "C:\\chromedriver.exe"
#######
#######browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)


def auto_page_pass(data_list):
    chrome_options = Options()
    '''
    ������� ��� ���������� ���������.
    '''
    chromedriver = homeDir + "\\sourses\\chromedriver.exe"      
    prefs = {"profile.default_content_settings.popups": 0,
                "download.default_directory": homeDir + "\data",                  
                "directory_upgrade": True}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    browser.get('https://websbor.gks.ru/online/info')
    sleep(5)
    #��� ������ �������� � ������� ������������ XPath (F12 � ��������, ����� ������� ��������, ��� - Copy - XPath)
    # ������ � ���� "������� � email" 123
    browser.find_element("xpath",'//*[@id="inn"]').send_keys(data_list)
    sleep(1)
    #������� ������ 1
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[1]').click()
    sleep(3)
    browser.quit()
    return 0




if __name__ == '__main__':

    #data.read_dataFile2()


    #for data_list in dataList:
    #    #print(data_list)
    auto_page_pass(data_list)
    #