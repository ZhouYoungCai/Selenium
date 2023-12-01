# -*- coding: UTF-8 -*-
# author: joker
# perject:web_python
# name:test_frame.py
# date:2023/8/9
from selenium.webdriver.common.by import By
from frame_window.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # 新版本的selenium已经删除了下面这种用法， 不推荐使用
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element(By.ID, "draggable").text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, "submitBTN").text)