"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login_page import LoginPage
from utils.log_utils import logger


class TestLitemall:

    # 前置动作
    def setup_class(self):
        # 用户登录
        self.browser = LoginPage().login()

    # 后置动作
    def teardown_class(self):
        self.browser.quit()

    # 新增功能
    def test_add_type(self):

        # 链式调用
        list_page = self.browser\
            .go_to_category_list()\
            .click_create()\
            .create_category("新增商品测试")\

        res = list_page.get_notification_msg("创建成功")
        list_page.delete_category("新增商品测试")

        # 断言
        assert "创建成功" == res



    # 删除功能
    def test_delete_type(self):

        # 链式调用
        res = self.browser \
            .go_to_category_list() \
            .click_create() \
            .create_category("删除商品测试") \
            .delete_category("删除商品测试")\
            .get_notification_msg("删除成功")

        # 断言
        assert "删除成功" == res

