from selenium import webdriver
from selenium.webdriver.common.by import By


def web_locate():
    # 首先需要实例化driver对象，Chrome()一定要加括号
    driver = webdriver.Chrome()
    # 打开一个网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 1. ID定位, 第一个参数传递定位方式，第二参数传递定位元素，调用这个方法的返回值为WebElement
    # web_element = driver.find_element(By.ID, "locate_id")
    # web_element = driver.find_element_by_id("locate_id")
    # print(web_element)
    # 2. Name定位，
    # 如果没有报错，证明元素找到了
    # 如果报错 no such element 代表，元素定位可能出现错
    # driver.find_element(By.NAME, "locate11111") #错误示例
    # driver.find_element(By.NAME, "locate")
    # 3. Css 选择器定位
    # driver.find_element(By.CSS_SELECTOR, "#locate_id > a > span")
    # 4. xpath 表达式定位
    # driver.find_element(By.XPATH, '//*[@id="locate_id"]/a/span')
    # 5. 通过链接文本的方式 （1） 元素一定是a标签 2. 输入的元素为标签内的文本
    # driver.find_element(By.LINK_TEXT, "元素定位")

if __name__ == '__main__':
    web_locate()