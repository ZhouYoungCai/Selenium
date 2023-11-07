1、selenium点击与输入
    find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
    find_element(By.ID,'su').click()
2、xpath定义
    XML path language
	用于解析html与xml
3、代码
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.by import By

class TestWait:
    def setup(self):
	    self.driver = webdriver.chrome()
		self.driver.get("https://www.baidu.com/")
	def test_wait(self):
	    self.driver.find_element(By.xpath,'//*[id="kw"]').sendkeys("霍格沃兹测试学院")