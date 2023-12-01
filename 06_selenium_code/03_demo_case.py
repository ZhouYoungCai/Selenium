#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

def test_search():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https:www.baidu.com/")
    driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("霍格沃兹测试学院")
    driver.find_element(By.CSS_SELECTOR,"#su").click()
    sleep(3)
    result = "霍格沃兹测试学院"
    assert "霍格沃兹测试学院" in result