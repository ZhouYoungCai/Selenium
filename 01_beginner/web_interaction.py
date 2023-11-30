import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 元素操作
def element_interaction():
    """
    元素的操作， 点击/输入/清空
    .send_keys("霍格沃兹测试开发")
    .clear()
    .click()
    :return:
    """
    # 1. 实例化driver对象
    driver = webdriver.Chrome()
    # 2. 打开一个网页
    driver.get("https://www.sogou.com/")
    # 3. 定位到输入框进行输入操作
    driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
    # 强制等待两秒
    time.sleep(2)
    # 4. 对输入框进行清空
    driver.find_element(By.ID, "query").clear()
    time.sleep(2)
    # 5. 再次输入
    driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发2")
    time.sleep(2)
    # 6. 点击搜索
    driver.find_element(By.ID, "stb").click()
    time.sleep(2)

# 获取元素属性
def element_get_attr():
    # 1. 实例化driver
    driver = webdriver.Chrome()
    # 2. 打开网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 3. 定位一个元素
    web_element = driver.find_element(By.ID, "locate_id")
    # 4. 打印这个元素对象
    # 断点打在想看的对象的下一行
    # print(web_element)
    # 5. 获取元素的文本信息
    # 不是每个元素都含有文本信息的。
    # print(web_element.text)
    # 6. 获取元素的属性信息，title="xxx"，
    # res = web_element.get_attribute("class")
    # print(res)


if __name__ == '__main__':
    # 元素操作
    # element_interaction()
    element_get_attr()