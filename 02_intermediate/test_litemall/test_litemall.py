"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLitemall:
    # 前置动作
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
    # 后置动作
    def teardown_class(self):
        self.driver.quit()

    # 登录功能
    def test_login(self):
        # 打开页面
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        # 问题，输入框内有默认值，此时send——keys不回清空只会追加
        # 解决方案： 在输入信息之前，先对输入框完成清空
        # 输入用户名密码
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        time.sleep(10)
    # 新增功能
    def test_add_type(self):
        # 登录
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        # 问题，输入框内有默认值，此时send——keys不回清空只会追加
        # 解决方案： 在输入信息之前，先对输入框完成清空
        # 输入用户名密码
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        # 窗口最大化
        self.driver.maximize_window()
        # 点击商场管理/商品类目，进入商品类目页面
        time.sleep(1)
        # 进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        # 添加商品类目操作
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("新增商品测试")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer .el-button--primary").click()
        # time.sleep(10)
        # finds 如果没找到会返回空列表， find 如果没找到则会直接报错
        # 如果没找到，程序也不应该报错
        res = self.driver.find_elements(By.XPATH, "//*[text()='新增商品测试']")
        # 断言产品新增后是否成功找到，如果找到，证明新增成功，如果没找到则新增失败
        # 判断查找的结果是否为空列表，如果为空列表证明没找到，反之代表元素找到，用例执行成功
        assert res != []

    # 删除功能
    def test_delete_type(self):
        # ================ 造数据步骤
        # 登录
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        # 问题，输入框内有默认值，此时send——keys不回清空只会追加
        # 解决方案： 在输入信息之前，先对输入框完成清空
        # 输入用户名密码
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        # 窗口最大化
        self.driver.maximize_window()
        # 点击商场管理/商品类目，进入商品类目页面
        time.sleep(1)
        # 进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        # 添加商品类目操作
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("删除商品测试")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer .el-button--primary").click()
        # ============完成删除步骤
        self.driver.find_element(By.XPATH, "//*[text()='删除商品测试']/../..//*[text()='删除']").click()
        # 断言： 删除之后获取这个 删除商品测试的 这个商品类目是否还能获取到，如果获取到，证明没有删除成功，反之删除成功
        time.sleep(2)
        res = self.driver.find_elements(By.XPATH, "//*[text()='删除商品测试']")
        assert res == []