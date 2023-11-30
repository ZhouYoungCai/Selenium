from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 定义配置的实例对象option
option = Options()
# 修改实例属性 为 debug 模式启动的 ip+端口
option.debugger_address = "localhost:9222"
# 实例化driver 的时候，添加option 配置
driver = webdriver.Chrome(options=option)
# driver = webdriver.Chrome()
# driver.get("https://work.weixin.qq.com/wework_admin/frame")
# 点击添加成员的操作
# driver.find_element_by_css_selector(".ww_indexImg_AddMember").click()
# 想要调试的步骤
driver.find_element_by_id("username").send_keys("hogwarts")