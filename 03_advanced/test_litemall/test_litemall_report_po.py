"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# ====问题1： 用例产生了脏数据，
# 解决方案： 清理对应的脏数据。清理的方式可以通过接口也可以通过ui的方式，数据的清理一定到放在断言操作之后完成，要不然可能会影响断言结果

# ====问题2： 代码存在大量的强制等待
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login_page import LoginPage
from utils.log_utils import logger


class TestLitemall:
    # 前置动作
    def setup_class(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()

    # 后置动作
    def teardown_class(self):
        # 退出浏览器
        self.home.do_quit()

    # 新增功能
    @pytest.mark.parametrize("category_name", ["a"])
    def test_add_type(self, category_name):
        list_page = self.home\
            .go_to_category()\
            .click_add()\
            .create_category(category_name)\

        # 断言
        res = list_page.get_operate_result()
        assert "创建成功" == res

        # 数据清理
        list_page.delete_category(category_name)


    # 删除功能
    @pytest.mark.parametrize("category_name", ["delA"])
    def test_delete_type(self, category_name):
        res = self.home\
            .go_to_category()\
            .click_add()\
            .create_category(category_name)\
            .delete_category(category_name)\
            .get_delete_result()

        assert "删除成功" == res

