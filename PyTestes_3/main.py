import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

nav = webdriver.Chrome()

nav.get('https://buger-eats.vercel.app/deliver')

nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[1]/div[1]/input').send_keys('Peter Peter Peter Peter')
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[1]/div[2]/input').send_keys('012.345.167-90')
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[2]/div[1]/input').send_keys('pedro@hotmail.com.br')
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[2]/div[2]/input').send_keys('999999999')
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[1]/div[1]/input').send_keys('60748-540')
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[1]/div[2]/input').click()
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[3]/div[1]/input').send_keys('555')
nav.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[3]/ul/li[1]').click()
nav.find_element('xpath', '//*[@id="page-deliver"]/form/div/input').send_keys(r"C:\Users\pedro\Downloads\jpg\Screenshot_1.jpg")
nav.find_element('xpath', '//*[@id="page-deliver"]/form/button').click()
