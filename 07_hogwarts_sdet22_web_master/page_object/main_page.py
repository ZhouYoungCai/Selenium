"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object.add_member_page import AddMemberPage
from page_object.base_page import BasePage
from page_object.contact_page import ContactPage
from page_object.wework_page import WeworkPage


class MainPageObject(WeworkPage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 跳转通讯录页面的功能
    def goto_contact_page(self):
        return ContactPage()

    # 跳转添加成员页面的功能
    def goto_add_member_page(self):
        # 点击添加成员按钮
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)

