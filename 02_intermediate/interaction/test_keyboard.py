"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestKeyboard:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_shift(self):
        """
        1. 访问 https://ceshiren.com/ 官方网站
        2. 点击搜索按钮
        3. 输入搜索的内容，输入的同时按着shift 键
        """
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # 1/ key down 代表按下某个键位
        # 2/ 输入内容
        # 3. 执行以上操作
        ActionChains(self.driver)\
            .key_down(Keys.SHIFT, ele)\
            .send_keys("selenium")\
            .perform()
        time.sleep(3)

    def test_enter(self):
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
        # 第一种回车方式
        # self.driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
        # 第二种回车方式
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(3)

    def test_copy_and_paste(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # 判断操作系统是否为mac如果是mac 则返回 command 键位， 如果是windows 返回 control键位
        command_control = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        ActionChains(self.driver) \
            .key_down(Keys.SHIFT, ele) \
            .send_keys("selenium!").\
            key_down(Keys.ARROW_LEFT).\
            key_down(command_control).send_keys("xvvvvvvvvvvvv").key_up(command_control).\
            perform()
        time.sleep(3)

