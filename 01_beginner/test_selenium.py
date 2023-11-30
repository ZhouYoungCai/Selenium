from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        # self.driver.quit()
        pass

    def test_selenium(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id("su").click()