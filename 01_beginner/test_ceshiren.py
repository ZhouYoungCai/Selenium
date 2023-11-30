"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 结合pytest测试框架
# 用例标题=文件名+类名+方法名
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#=============优化1
#问题： 1. 没有前置和后置的处理动作 2. driver启动了之后没有做quit()
# 如果没有quit()动作，会导致大量的 chromedriver 进程一直存在 mac 使用 ps -ef | grep chromedriver， window 看任务管理期

class TestCeshiren:

    def setup(self):
        """
        前提条件： 进入测试人论坛的搜索页面
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # 打开被测地址
        self.driver.get("https://ceshiren.com/search?expanded=true")

    def teardown(self):
        # 优化问题： 2. driver启动了之后没有做quit()
        # 每一次用例结束之后都会关闭chromedriver的进程，也会关闭浏览器
        self.driver.quit()

    # def test_search2(self):
        # self.driver.

    def test_search(self):
        """
        测试步骤： 1. 输入搜索关键词
                  2. 点击搜索按钮
        预期结果/实际结果
        :return:
        """
        # 打开浏览器

        # 定位到搜索输入框，并输入搜索内容
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='搜索']").send_keys("appium")
        # 定位到搜索按钮，并点击
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        # 断言=预期结果与实际结果对比的结果
        # 获取实际结果， 即为获取搜索结果列表的标题内容
        # 第一种方式，获取第一个搜索结果，
        # time.sleep(3) # 加一个3秒的强制等待，等待页面渲染完成，如果没有报错，证明定位没有错误，反之，可能定位或者其他原因的错误
        web_element=self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        # 获取文本类的实际结果 断言，appium关键字是否在获取的实际结果文本之中
        # 两种解决方案： 1. 统一，比如 断言 Appium in
        # 2. 就是把获取到的内容和预期结果同意 使用.lower 就可以使大写的字母小写
        assert "appium" in web_element.text.lower()