"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.log_utils import logger

"""首页"""

class HomePage(BasePage):

    __MENU_MALL_MANAGE = (By.XPATH, "//*[text()='商场管理']")
    __MENU_PRODUCT_CATEGORY = (By.XPATH, "//*[text()='商品类目']")

    """系统首页：进入商品类目"""
    def go_to_category(self):
        logger.info("系统首页：进入商品类目")

        # 点击菜单“商场管理”
        self.do_find(self.__MENU_MALL_MANAGE).click()
        # 点击菜单“商品类目”
        self.do_find(self.__MENU_PRODUCT_CATEGORY).click()

        # ==》类目列表页面
        from page_objects.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
