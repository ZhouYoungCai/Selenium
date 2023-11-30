"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.log_utils import logger

"""登录页面"""

class LoginPage(BasePage):

    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/#/login"

    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button--primary")

    """登录页面：用户登录"""
    def login(self):
        logger.info("登录页面：用户登录")
        # 访问登录页
        logger.info("访问登录页")
        # 输入“用户名”
        self.do_send_keys("manage", self.__INPUT_USERNAME)
        # 输入“密码”
        self.do_send_keys("manage123", self.__INPUT_PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BTN_LOGIN).click()

        # ==》首页
        from page_objects.home_page import HomePage
        return HomePage(self.driver)