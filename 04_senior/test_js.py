"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_taobao_js():
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com/")
    driver.implicitly_wait(3)

    driver.execute_script("document.querySelector('#J_SiteNavMytaobao').className='site-nav-menu site-nav-mytaobao site-nav-multi-menu J_MultiMenu site-nav-menu-hover'")
    driver.find_element(By.XPATH, "//*[text()='已买到的宝贝']").click()
    time.sleep(5)
    driver.quit()


def test_12306_js():
    driver = webdriver.Chrome()
    driver.get("https://www.12306.cn/index/")
    driver.implicitly_wait(3)
    # 修改时间控件的信息
    driver.execute_script('document.querySelector("#train_date").value="2023-12-24"')
    # 获取时间控件的信息，并返回出来
    date_data = driver.execute_script('return document.querySelector("#train_date").value')
    print(f"获取的时间控件信息为{date_data}")


