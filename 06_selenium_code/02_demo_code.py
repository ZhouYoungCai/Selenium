#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

bro = webdriver.Chrome()
bro.maximize_window()
sleep(3)
bro.get("https://www.mail.qq.com/")
sleep(3)
bro.switch_to_frame("login_frame")
sleep(3)
bro.find_element(By.ID,"u").send_keys("1121822552")
sleep(1)
bro.find_element(By.ID,"p").send_keys("zhou1234")
sleep(1)
bro.find_element(By.ID,"login_button").click()
sleep(3)
bro.switch_to_default_content()
bro.find_element(By.LINK_TEXT,"基本版").click()
sleep(3)
bro.quit()