# -*- coding: UTF-8 -*-
# author: joker
# perject:web_python
# name:base.py
# date:2023/8/9
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()