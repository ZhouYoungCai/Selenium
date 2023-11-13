01、目录
	PageObject 设计思想
	PageObject 企业微信建模
	PageObject 自动化测试实战演练
02、用户端自动化测试学习思路

03、什么时候需要做 UI 自动化测试
	业务流程不频繁改动
	UI 元素不频繁改动
	需要频繁回归的场景
	核心场景等
04、UI 自动化测试需要哪些技术
	Web 自动化测试
	Selenium
	Cypress
	Airtest
	App 自动化测试
	Appium
	ATX
	Airtest
05、Selenium
    Selenium is a suite of tools to automate web browsers across many platforms. 
	runs in many browsers and operating systems. 
	can be controlled by many programming languages and testing frameworks
06、Web 自动化测试流程
    测试用例设计：与手工测试一致
	功能测试场景：
	UI 自动化测试场景：
07、PageObject 设计思想
    为什么需要 PageObject 设计模式：
		降低UI变化导致的测试用例脆弱性问题
		让用例清晰明朗，与具体实现无关
08、一个添加成员的步骤
	登录_login 页面
	登录后进入首页_main 页面
	点击添加成员_main 页面
	填写添加信息_add_member 页面
	点击保存_add_member 页面
	返回通讯录_add_membe 页面
	加断言做验证_contact 页面
09、传统的 web 测试用例
	# 对应自动化测试代码
	def test_add_member(self):
	   self.driver.get(“https://work.weixin.qq.com/wework_admin/frame#index")
	   element_locator = (By.LINK_TEXT, "添加成员")
		WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
		self.driver.find_element(*element_locator).click()
		self.driver.find_element(By.NAME, 'username').send_keys("abc")
		self.driver.find_element(By.NAME, 'english_name').send_keys("abc")
		self.driver.find_element(By.NAME, "acctid").send_keys("abc")
		self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_zipCode_input input').click()
		self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="853"]').click()
	   assert...
10、如果需要多添加一个步骤
	从首页->通讯录->添加成员应该怎么改

	登录_login 页面
	进入首页_main 页面
	点击通讯录_main 页面
	点击添加成员_contact 页面
	填写添加信息_add_member 页面
	点击保存_add_member 页面
	返回通讯录_add_member 页面
	加断言做验证_contact 页面
11、传统的 web 测试用例
	#对应的自动化测试代码

	def test_add_member(self):
	   self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
	   element_locator = (By.LINK_TEXT, "添加成员")
		WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_locator))
		self.driver.find_element(*element_locator).click()
		self.driver.find_element(By.NAME, 'username').send_keys("abc")
		self.driver.find_element(By.NAME, 'english_name').send_keys("abc")
		self.driver.find_element(By.NAME, "acctid").send_keys("abc")
		self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_zipCode_input input').click()
		self.driver.find_element(By.CSS_SELECTOR, 'li[data-value="853"]').click()
	   assert...
12、Java版本代码
	public class DemoTest {

		public static WebDriver driver ;
		private WebDriverWait wait;

		@BeforeAll
		void setupAll() {
			System.setProperty(
					"webdriver.chrome.driver",
					"/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_95.0.4638.54"
			);
	//        WebDriver driver = new FirefoxDriver();
			driver = new ChromeDriver();
			wait = new WebDriverWait(driver, Duration.ofSeconds(10));
		}

		@AfterAll
		void teardownAll() {
			driver.quit();
		}
13、传统 UI 自动化测试用例的问题
	无法适应 UI 变化，UI 变化会导致大量的 case 需要修改
	无法清晰表达业务用例场景
	大量的样板代码 driver find click
14、PageObject 原理以及六大原则
	selenium 官方网站
	马丁福勒个人博客
15、PO 设计思想
	页面 ==> 类
	属性（名词）：元素
	方法（动词）：功能
	设计思想
16、PO 六大原则
    六大原则：
	1. 公共的方法代表也买你提供的服务
　　2. 不要暴露细节
　　3. 不要把断言和操作细节混用
　　4. 方法可以return到新打开的页面
　　5. 不要把整页的内容都放到PO中
　　6. 相同的行为会产生不同的结果，可以封装不同结果
    原则一：要封装页面中的功能或服务，比如点击页面元素，可以进入到新的页面，则可为这个服务封装方法"进入新页面"
　　原则二：封装细节，对外只提供方法名（或者接口）
　　原则三：封装的操作细节中不要使用断言，把断言放到单独的模块中，比如：testcase
　　原则四：点击一个按钮会开启新的页面，可以用return方法便是跳转，比如return MainPage()表示跳转到主页
    原则五：只为页面中重要的元素进行PO设计，舍弃不重要的内容
　　原则六：一个动作可能产生不同结果，比如点击按钮后，可能成功，也可能失败，为两种结果封装两个方法：click_success和click_error
17、原则解读
	方法意义
	用公共方法代表 UI 所提供的功能
	方法应该返回其他的 PageObject 或者返回用于断言的数据
	同样的行为不同的结果可以建模为不同的方法
	通常不在方法内加断言
	字段意义
	不要暴露页面内部的元素给外部
	不需要建模 UI 内的所有元素
18、企业微信PageObject建模
	黄色的方块代表一个类
	每条线代表这个页面提供的方法
	箭头的始端为开始页面
	箭头的末端为跳转页面或需要断言的数据
19、PO 自动化测试实战演练
    实战练习思路
	梳理测试用例
	根据业务逻辑编写，添加断言
	通过链式调用更加方便描述业务逻辑
	具体的实现先设置为空
	梳理用例执行前动作和执行后动作，考虑脏数据清理等问题。
20、填充实现-Driver 初始化、BasePage 封装
	问题：
	Driver 初始化如果绑定在某个页面类中，那么多个页面类都需要进行初始化操作
	解决方案：
	Driver 初始化的部分放在 BasePage 中，其他 Page 类继承 BasePage。
	子类可以使用父类的属性，直接通过 self.driver 调用 driver 实例对象
21、填充实现-构造 PO 模型类图
	分为三层
	具体业务层
	公共业务层
	和业务无关的公共方法层
22、优化用例-封装样板代码
	问题：
	直接调用 selenium API，导致存在大量的样板代码，find、finds 等。
	解决方案：
	常用的 UI 操作封装在 base_page 中。
23、优化用例-提取页面元素
	问题：
	页面定位写在每个 Page 的方法中，如果此页面定位存在多处复用，那么需要多处修改
	解决方案：
	将页面定位抽离为私有类变量，符合六大原则中不要暴露页面内部的元素给外部
24、优化用例-添加起始页面的 url
	问题：
	起始 url 不应该写在 basepage 中，basepage 和具体业务没有任何关联。
	每个 UI 用例的开始不可能都从首页开始，有的可能是从其他页面开始。
	解决方案：
	每个 Page 子类添加_base_url 变量。
	在base_page中添加back_page的方法。可以返回用例的初始状态
25、为什么要学习复用浏览器
    自动化测试过程中，存在人为介入场景
	提高调试UI自动化测试脚本效率
26、复用浏览器配置步骤
    1、需要退出当前所有的谷歌浏览器（特别注意）
	2、输入启动命令，通过命令启动谷歌浏览器
	    找到chrome的启动路径
		配置环境变量
	3、验证是否启动成功
27、cookie是什么？
    cookie是一些数据，存储于你电脑上的文本文件中
	当web服务器向浏览器发送web页面时，在连接关闭后，服务端不会记录用户的信息
28、为什么要使用cookie自动化登录
    复用浏览器仍然在每次用例开始都需要人为介入
	若用例需要经常执行，复用浏览器则不是一个好的选择
	大部分cookie的时效性都很长，扫一次可以使用多次
29、使用cookie实现自动化登录的思路
    打开浏览器，扫码登录
	确保登录之后（重点！），通过get_cookie获取cookie
	检查本地文件是否已经获取成功
	再次打开浏览器，通过cookie直接进入主页
30、常见问题
    1、登录企业微信cookie有互踢机制。在获取cookie成功之后，不要再进行扫码操作
	2、获取cookie的时候，即执行代码get_cookie()时，一定要确保已经登录
	3、植入cookie之后需要进入登录页面，刷新验证是否自动登录成功
31、使用cookie登录
    获取：cookie driver.get_cookies()
	添加：cookie driver.add_cookie(cookie)