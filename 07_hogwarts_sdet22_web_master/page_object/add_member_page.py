"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_object.contact_page import ContactPage
from page_object.wework_page import WeworkPage


class AddMemberPage(WeworkPage):
    # 页面元素不要暴露出去，只给页面的方法提供使用。
    _INPUT_USERNAME = (By.ID, "username")


    def add_member(self, username, accid, phone):
        """
        添加成员功能
        ，添加成功后返回通讯录页面
        """
        # 问题： driver实例化了多次，影响用例的执行
        # 解决方案： 让driver 只实例化一次
        # self.driver.find_element(By.ID, "username").send_keys("金克斯3")
        self.find(self._INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self, username, accid, phone):
        self.find(self._INPUT_USERNAME).send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [ele.text for ele in eles]
        return error_list

