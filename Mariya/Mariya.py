#coding=1251
from http.client import responses
from ssl import Options
from tkinter import BROWSE
from urllib import response
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import data_inn


#������ ���� ������ ��� �������� ������� ���� �����
#� ��������� �� ����������� ���������� � ������� ������� ��������� �����

chromeOptions = webdriver.ChromeOptions()

#!!!!!!!!!!!!!!���� --- ��� ��������� �� ����� ������ ��� ��� ���� ��������� 
#���������� ����� ���������� �� Path � ����� ��� ��� ��� ����� ����������
prefs = {"download.default_directory" : "C:\\Users\\igorm\\Downloads\\test"}
chromeOptions.add_experimental_option("prefs",prefs)

#��������!!!!!!!!!!!!!!!!!!!!�� ������ ������� ��������� webdriver
chromedriver = "C:\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
browser.get('https://websbor.gks.ru/online/info')
sleep(1)


#inn = data_inn.inn
inn = data_inn.data_inject()
def auto_page_pass():
    #��� ������ �������� � ������� ������������ XPath (F12 � ��������, ����� ������� ��������, ��� - Copy - XPath)
    # ������ � ���� "������� � email" 123
    browser.find_element("xpath",'//*[@id="inn"]').send_keys(inn)
    #������� ������ 1
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
    sleep(1)
    browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[1]').click()
    sleep(1)
pass



if __name__ == '__main__':

    
    auto_page_pass()
