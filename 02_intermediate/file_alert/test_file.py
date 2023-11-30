# -*- coding: UTF-8 -*-
# author: joker
# perject:web_python
# name:test_file.py
# date:2023/8/9
from time import sleep
from selenium.webdriver.common.by import By
from file_alert.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element(By.ID, "sttb").click()
        self.driver.find_element(By.ID, "stfile").send_keys(r"D:\Python_Project\web_python\web_python\file_alert\baidu.png")
        sleep(3)