#coding:utf-8
from selenium import webdriver
from time import *

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    sleep(2)
    driver.quit()