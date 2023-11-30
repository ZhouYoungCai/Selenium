# -*- coding: UTF-8 -*-
# author: joker
# perject:web_python
# name:test_window.py
# date:2023/8/9
from time import sleep
from selenium.webdriver.common.by import By
from frame_window.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 窗口切换
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("13800000000")

        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()

        sleep(3)
