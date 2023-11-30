from selenium import webdriver
from selenium.webdriver.by import By


def test_search():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https:www.baidu.com/")
    driver.find_element_by_css_selector("#kw").send_keys("霍格沃兹测试学院")
    driver.find_element_by_css_selector("#su").click
    result = find_element_by_css_selector(".result:nth-child(2)>h3>a>em").text
    assert "霍格沃兹测试学院" in result