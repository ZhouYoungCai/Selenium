"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 打开浏览器
import time

from selenium import webdriver


def open_browser():
    driver = webdriver.Chrome()
    # 调用get 方法时需要传递浏览器的url
    driver.get("https://ceshiren.com/")
    time.sleep(2)
    # 刷新浏览器
    # driver.refresh()
    # 通过get跳转到baidu
    # driver.get("https://www.baidu.com/")
    # 返回百度之前的页面，也就是测试人页面
    # driver.back()
    # 最大化浏览器
    driver.maximize_window()
    time.sleep(2)
    driver.minimize_window()
    time.sleep(2)



# 最大化

# 最小化

if __name__ == '__main__':
    # 1. 打开浏览器
    # 2. 刷新浏览器
    open_browser()