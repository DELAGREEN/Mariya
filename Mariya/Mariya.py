from http.client import responses
from ssl import Options
from urllib import response
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os



#������ ���� ������ ��� �������� ������� ���� �����
#� ��������� �� ����������� ���������� � ������� ������� ��������� �����
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "D:\\Downloads\\test"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)


browser.get('https://websbor.gks.ru/online/info')
sleep(1)
#��� ������ �������� � ������� ������������ XPath (F12 � ��������, ����� ������� ��������, ��� - Copy - XPath)
# ������ � ���� "������� � email" 123
eml = browser.find_element("xpath",'//*[@id="inn"]').send_keys('5260477034')
#������� ������ 1
browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
sleep(1)
browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
sleep(1)
browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[1]').click()
sleep(1)

