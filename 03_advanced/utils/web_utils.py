"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os.path
import time
import allure
from selenium.webdriver.support import expected_conditions

from utils.log_utils import logger


def click_exception(by, element, max_attempts=5):
    """自定义显式等待条件"""

    def _inner(driver):
        # 多次点击按钮
        actul_attempts = 0 # 实际点击次数
        while actul_attempts<max_attempts:
            # 进行点击操作
            actul_attempts += 1 # 每次循环，实际点击次数加1
            try:
                # 如果点击过程报错，则直接执行 except 逻辑，并切继续循环
                # 没有报错，则直接return 循环结束
                driver.find_element(by, element).click()
                return True
            except Exception:
                logger.debug("点击的时候出现了一次异常")
        # 当实际点击次数大于最大点击次数时，结束循环并抛出异常
        raise Exception("超出了最大点击次数")
    # return _inner() 错误写法
    return _inner


def display_exception(value, by, element):
    """自定义显式等待条件"""
    element = element.format(value)
    expect = expected_conditions.visibility_of_any_elements_located((by, element))
    return expect


def ui_exception_record(func):
    def inner(*args, **kwargs):
        driver = args[0].driver
        try:
            # 被装饰的函数执行过程中，如果出现异常就捕获，并且完成数据记录操作
            return func(*args, **kwargs)
        except Exception:
            # 如果查找元素时抛出异常，则截图/日志/pagesource
            # 截图记录，双重保障
            logger.warning("查找元素出现异常")
            timestamp = int(time.time())
            # 注意：！！ 一定要提前创建好images 路径
            image_path = f"./data/image_data/image_{timestamp}.PNG"
            page_source_path = f"./data/page_source_data/page_source_{timestamp}.html"
            driver.save_screenshot(image_path)
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(driver.page_source)
                # 涉及报告信息，所以使用命令行执行才能看到报告效果
            allure.attach.file(image_path, name="picture",
                               attachment_type=allure.attachment_type.PNG)
            # allure.attach.file(page_source_path, name="page_source",
            #                    attachment_type=allure.attachment_type.HTML)
            # 如果想看的是转换页面前的html 源码，那么需要使用text 格式
            allure.attach.file(page_source_path, name="page_source",
                               attachment_type=allure.attachment_type.TEXT)
            raise Exception
    return inner
