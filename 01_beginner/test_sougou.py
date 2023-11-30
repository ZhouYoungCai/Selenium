# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test():
  def setup_method(self, method):
    # 前提条件
    self.driver = webdriver.Chrome()
    self.vars = {}

  # 后置动作
  def teardown_method(self, method):
    self.driver.quit()

  # 测试用例步骤
  def test_sougou(self):
    # 打开网页，设置窗口
    self.driver.get("https://www.sogou.com/")
    self.driver.set_window_size(1235, 693)
    # 输入搜索信息
    self.driver.find_element(By.ID, "query").click()
    self.driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
    # 点击搜索
    self.driver.find_element(By.ID, "stb").click()
    element = self.driver.find_element(By.ID, "stb")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 问题： 无法确定用例执行成功或失败
    # 解决方案： 添加断言信息，判断搜索列表中，是否含有霍格沃兹测试开发
    res_element = self.driver.find_element(By.CSS_SELECTOR, "#sogou_vr_30000000_0 > em")
    # 获取到定位的文本信息
    # 判断实际获取到的搜索展示的列表和预期的是否一致
    assert  res_element.text == "霍格沃兹测试开发32132131"

