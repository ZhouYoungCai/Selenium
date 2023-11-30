"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_options():
    # 在实例化driver 对象之前，需要先定义好配置信息
    options = webdriver.ChromeOptions()
    # 在浏览器启动之前，就配置完成，窗口最大化的配置
    options.add_argument("start-maximized")
    # 指定浏览器分辨率
    options.add_argument('window-size=1920x3000')
    #无头模式： 浏览器不回显示的启动在机器上。
    options.add_argument('--headless')
    # 实例化一个driver 对象，注意： 配置对象options 要通过 chrome_options参数添加
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://ceshiren.com/")
    # 获取登录按钮中的文本信息
    login_text = driver.find_element(By.CSS_SELECTOR, ".login-button").text
    print(login_text)