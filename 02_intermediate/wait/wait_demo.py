"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

if __name__ == '__main__':

    driver = "aaaa"
    def fake_conditions(driver):
        print("当前的时间为", time.time())
    # until 传入的参数为一个函数对象，不是函数的调用
    # WebDriverWait(driver, 10, 2).until(fake_conditions())
    WebDriverWait(driver, 10, 2).until(fake_conditions, "霍格沃兹测试开发")