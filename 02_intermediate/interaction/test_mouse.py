"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestMouse:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_double_click(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        # self.driver.find_element(By.ID, "primary_btn").click()
        ele = self.driver.find_element(By.ID, "primary_btn")
        # 调用 双击方法， 传入被双击的元素
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(3)

    def test_drap_and_drop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        # 获取起始元素的位置
        start_ele = self.driver.find_element(By.ID, "item1")
        # 获取目标元素的位置
        target_ele =  self.driver.find_element(By.ID, "item3")
        # 实现拖拽操作
        ActionChains(self.driver).drag_and_drop(start_ele, target_ele).perform()
        time.sleep(3)

    def test_move_element(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        ele = self.driver.find_element(By.CSS_SELECTOR, ".menu")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.XPATH, "//*[contains(text(),'管理班')]").click()
        time.sleep(3)
