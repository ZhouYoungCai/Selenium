# -*- coding: UTF-8 -*-
# author: joker
# perject:web_python
# name:test_alert.py
# date:2023/8/9
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from file_alert.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        # 点击拖拽到drop
        action.drag_and_drop(drag, drop).perform()
        # sleep(2)
        print("点击 alert 确认")
        # 获取当前页面的警告框，接受警告框
        self.driver.switch_to.alert.accept()
        # 切换回默认的frame下，即切换回主文档
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        sleep(3)