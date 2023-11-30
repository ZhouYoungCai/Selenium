"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver

from senior.test_muliti_browser.conftest import web_env


class TestBrowser:

    def setup_class(self):
        self.browser = web_env.get("browser")

    def test_ceshiren(self):
        print(f"获取到的浏览器信息为{self.browser}")
        if self.browser == "firefox":
            self.driver =webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.quit()
        assert False