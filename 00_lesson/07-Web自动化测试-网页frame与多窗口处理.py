1、selenium里面如何处理多窗口场景
    多窗口识别
	多窗口之间切换
2、selenium里面如何处理frame
    多个frame识别
	多个frame之间切换
3、多窗口处理
    点击某些链接，会重新打开一个窗口，对于这种情况，想在新页面上操作，就得先切换窗口。
	获取窗口的唯一标识用句柄表示，所以只需要切换句柄，就可以在多个页面灵活操作了。
4、多窗口处理流程：
    1、先获取到当前窗口句柄（driver.current_window_handle）
	2、再获取到所有的窗口句柄（driver.window_handles）
	3、判断是否是想要操作的窗口，如果是，就可以对窗口进行操作。
	   如果不是，跳转到另外一个窗口，对另外一个窗口进行操作（driver.switch_to_window）
5、frame介绍
    在web自动化中，如果一个元素定位不到，name很大可能是在iframe中。
	什么是frame？
	    frame是HTML中的框架，在html中，所谓的框架就是可以在同一个浏览器中显示不止一个页面
		基于html的框架，又分为垂直框架和水平框架
	frame分类？
	    frame标签包含frameset、frame、iframe三种
		frameset和普通的标签一样，不会影响正常的定位，可以使用index、id、name、webeleement任意方式定位frame
		而frame与iframe对selenium定位而言是一样的。selenium有一组方法对frame进行操作。
	演示：https://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols
6、多frame切换
    frame存在两种：一种是嵌套的，一种是未嵌套的
	切换frame：
	    driver.switch_to.frame() #根据元素id或者index切换frame
		driver.switch_to.default_content()  #切换到默认frame
		driver.switch_to.parent_frame()  #切换到父级frame
7、处理未嵌套的iframe
    driver.switch_to_frame("frame的id")
	driver.switch_to_frame("frame-index")frame无ID的时候依据索引来处理
	索引从0开始driver.switch_to_frame(0)
	