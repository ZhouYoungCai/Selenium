1、selenium的介绍
    selenium支持web浏览器的自动化。它主要由3个工具构成，
	webdriver:手动写脚本
	IDE：录制脚本
	Grid：分布式
	官方网站：https://www.selenium.dev/
2、selenium环境配置步骤
    1、准备好python环境
	2、准备好selenium环境
	3、下载浏览器对应的driver版本
	4、driver配置环境变量
	5、在python中import对应的依赖
3、selenium的安装
    前提：
	    配置好python环境
		配置好pip工具
	安装： 
	     pip install selenium
		 或者在pycharm直接安装
4、driver的下载
    谷歌浏览器驱动，官方网站：https://chromedriver.storage.googleapis.com/index.html
	淘宝镜像：https://npm.taobao.org/mirrors/chromedriver/
5、python中如何使用
    import selenium
	from selenium import webdriver
	def test_selenium():
	    driver = webdriver.Chrome()
		driver.get("https://www.baidu.com/")
		