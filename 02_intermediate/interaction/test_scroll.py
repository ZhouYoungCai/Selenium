"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestScroll:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_scroll_to_element(self):
        self.driver.get("https://ceshiren.com/")
        ele = self.driver.find_element(By.XPATH, "//*[text()='怎么写高可用集群部署的测试方案？']")
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(10)

    def test_scroll_to_xy(self):
        self.driver.get("https://ceshiren.com/")
        ActionChains(self.driver).scroll_by_amount(0, 10000).perform()
        time.sleep(10)
