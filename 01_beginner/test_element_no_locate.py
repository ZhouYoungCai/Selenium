"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 定义一个测试类，代表元素定位不到的各种可能性，每个测试方法，对应一个场景
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementNoLocate:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_locator_error(self):
        """
        NoSuchElementException
        原因：在elements 中搜索对应的元素，发现没有搜索到，就证明定位写错了
        解决方案： 写一个正确的定位
        :return:
        """
        self.driver.get("https://vip.ceshiren.com")
        self.driver.find_element(By.ID, "xxxxxx")

    def test_locate_loading(self):
        """
        NoSuchElementException
        原因： 由于页面加载速度，元素还未加载出来就执行了find_element操作。
        debug思路： 添加一个强制等待，确认页面加载完成之后，再执行find操作，如果此时用例通过，代表定位没有问题，反之，可能就是别的原因
        解决方案：确认由于页面加载速度的问题的话，添加隐式等待配置或者显示等待。
        :return:
        """
        self.driver.get("https://vip.ceshiren.com")
        # time.sleep(5)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[text()='个人中心']")

    def test_dynamic_ID(self):
        """
        NoSuchElementException
        原因：因为ID是动态的，一直在变化的，所以此时使用ID定位就会非常不稳定
        解决方案：使用其他的定位方式，比如xpath 或者 css相对定位的方式
        :return:
        """
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        self.driver.find_element(By.XPATH, "//*[text()='动态id']").click()
        self.driver.find_element(By.XPATH, "//*[text()='动态id_1']")
        # self.driver.find_element(By.ID, "71")

    def test_iframe(self):
        """
        NoSuchElementException
        原因：排除 动态ID，页面渲染，定位编写错误的问题后，还有可能性为iframe
        debug过程： 1. 浏览器的elements页面输入iframe，确认页面含有iframe
                   2. 然后查看被定位的元素是否包含在iframe内，如果是的话，那么定位之前需要做切换iframe的操作
        :return:
        """
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        time.sleep(3)
        iframe_ele = self.driver.find_element(By.CSS_SELECTOR, ".iframe")
        self.driver.switch_to.frame(iframe_ele)
        self.driver.find_element(By.ID, "lianxi").click()

    def test_windows(self):
        """
        NoSuchElementException
        原因：打开了新窗口，并且定位的是新窗口里面的元素
        debug思路：在报错前一步骤，是否有打开新窗口操作
        解决方案：如果要定位新窗口的元素，那么需要先切换到对应的页面再去定位
        :return:
        """
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        self.driver.find_element(By.ID, "openWindows").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.ID, "lianxi").click()

