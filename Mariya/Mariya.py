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
#headers = {
#    " Accept": "application/json, text/plain, */*",  
#    " User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36 "
#    " charset=utf-8 "
#} 
#url = "https://websbor.gks.ru/online/info"
#
#r = requests.get(url, headers)
#src = r.text
#print
#(src)




#Данный блок служит для создания профиля Гугл хрома
#В частности он редактирует директорию в которую браузер загружает файлы
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "D:\\Downloads\\test"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)


browser.get('https://websbor.gks.ru/online/info')
sleep(1)
#для поиска элемента в примере используется XPath (F12 в браузере, поиск нужного элемента, ПКМ - Copy - XPath)
# ввести в поле "Телефон и email" 123
eml = browser.find_element("xpath",'//*[@id="inn"]').send_keys('5260477034')
#нажатие кнопки 1
browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[1]/div/form/div[3]/button/span').click()
sleep(1)
browser.find_element("xpath",'//*[@id="body"]/websbor-statistics-codes/websbor-simple-background/div/article/div/div[2]/div/button/span').click()
sleep(1)
browser.find_element("xpath",'//*[@id="mat-menu-panel-0"]/div/button[1]').click()
sleep(1)

