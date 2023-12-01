"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.wework_page import WeworkPage


class ContactPage(WeworkPage):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        pass

    def get_member_list(self):
        """
        获取成员列表
        :return:
        """
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_tr td:nth-child(2)")
        # 把元素列表 转换为名称列表，使用列表推导式（python-列表）
        member_list = [ele.text for ele in ele_list]
        # 成员的名称的列表
        return member_list