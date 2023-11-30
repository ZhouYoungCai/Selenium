"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ceshiren_ca():
    # mac
    # capability = {"platformName": "mac"}
    capability = {"platformName": "windows"}
    driver = webdriver.Chrome(desired_capabilities=capability)
    driver.get("https://ceshiren.com/")

def test_ceshiren_grid():
    # 1. 本地执行代码调通
    # 2. 切换为webdriver.remote
    # driver = webdriver.Chrome()
    executor_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"
    capabilities = {"browserName":"chrome","browserVersion":"99.0"}
    # capabilities = {"browserName":"firefox"}
    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities
    )
    driver.implicitly_wait(3)
    driver.get("https://ceshiren.com/")
    login_text = driver.find_element(By.CSS_SELECTOR, ".login-button").text
    print(login_text)
