"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_sleep():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    # driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错,
    # ==== 问题：由于页面加载比较慢，所以当执行find——element时，页面还没有加载完成，所以代码报错
    # =====解决方案： 等待页面加载完成
    # 添加强制等待, 设定一个页面能够加载完的时间，强行等待。确定页面加载完之后，再执行后面的代码就不回报错了
    # time.sleep(10)
    # 强制等待的问题： 1. 降低用例执行效率 2. 设置时间短的话还有可能出现报错
    # 这个原因导致，正式使用的自动化测试用例基本不会有强制等待的代码，通常会结合显式等待与隐式等待解决元素加载的问题
    # ====隐式等待=========================
    # driver.implicitly_wait(5) # 即使没有使用强制等待，依然不会报错
    # 结合find_element使用，当每次调用find_element且添加了隐式等待时，那么就会执行
    # 轮询的逻辑
    # driver.find_element(By.XPATH, "//*[text()='个人中心']")
    # 更改隐式等待最长时间
    # driver.find_element(By.XPATH, "//*[text()='个人中心']")
    # ======显式等待=======================
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # driver.implicitly_wait(3)
    # 隐式等待无法解决的点击问题
    # WebDriverWait 传入 driver 和 超时时间
    # until 可以结合expected_conditions.element_to_be_clickable()使用，需要传入一个元组对象(定位方式, 定位元素)
    # 再10秒内轮询去判断元素是否可以点击，如果超出10秒则会报错
    # 涉及到元素交互的时候，显式等待比隐式等待好用
    WebDriverWait(driver,  10).until(expected_conditions.element_to_be_clickable((By.ID, "success_btn")))
    driver.find_element(By.ID, "success_btn").click()
    time.sleep(5)


if __name__ == '__main__':
    wait_sleep()