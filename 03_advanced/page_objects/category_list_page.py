"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.log_utils import logger


class CategoryListPage(BasePage):
    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH, '//p[contains(text(), "创建")]')
    __MSG_DELETE_OPERATE = (By.XPATH, '//p[contains(text(), "删除")]')

    """类目列表页面：点击添加"""

    def click_add(self):
        logger.info("类目列表页面：点击添加")
        # 点击“添加”按钮
        self.do_find(self.__BTN_ADD).click()

        # ==》创建类目页面
        from page_objects.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    """类目列表页面：获取操作结果"""

    def get_operate_result(self):
        logger.info("类目列表页面：获取创建操作结果")
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        # 消息文本
        msg = element.text
        logger.info(f"冒泡消息是：{msg}")

        # ==》返回消息文本
        return msg

    def delete_category(self, category_name):
        logger.info("类目列表页面：删除操作")
        # 对指定对类目进行删除
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()

        # ==》跳转到当前页面
        return CategoryListPage(self.driver)

    """类目列表页面：获取操作结果"""

    def get_delete_result(self):
        logger.info("类目列表页面：获取删除操作结果")
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_DELETE_OPERATE)
        # 消息文本
        msg = element.text
        logger.info(f"冒泡消息是：{msg}")

        # ==》返回消息文本
        return msg
