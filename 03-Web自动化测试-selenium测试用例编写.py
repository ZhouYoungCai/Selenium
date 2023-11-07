1、目录 
    测试用例的核心要素
	selenium中如何编写测试用例
2、测试用例的核心要素
    一条测试用例的最终结果只有一个：成功或者失败
	三大核心要素为：
	    标题：是对测试用例的描述
		步骤：对测试执行过程进行描述
		断言：实际结果与预期结果对比
3、selenium中如何编写测试用例
    步骤：
	    打开页面：https:www.baidu.com/
        输入框输入搜索内容：霍格沃兹测试学院
		点击搜索按钮
		找到结果并断言
	代码：
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
	