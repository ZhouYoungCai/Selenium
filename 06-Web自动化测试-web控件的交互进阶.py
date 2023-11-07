1、常用的操作事件
    右键点击、页面滑动、单表操作等。
2、Actions
    官方文档：https://selenium-python.readthedocs.io/api.html
	ActionChains:执行PC端的鼠标点击、双击、右键，拖拽等事件
	TouchActions：模拟PC和移动端的点击，滑动，拖拽。多点触控等多种手势操作
3、动作链接ActionChains
    执行原理：
	    调用ActionChains的方法时，不会立即执行，而是将所有的操作，按顺序存放在一个队列里，
		当你调用perform()方法时，队列中的事件会依次执行
	基本用法：
	    生成一个动作action=ActionChains(driver)
		动作添加方法1 action.方法1
		动作添加方法2 action.方法2
		调用perform()方法执行(action.perform())
4、ActionChains用法1
    action = ActionChains(driver)
	action.click(element)
	action.double_click(element)
	action.context_click(element)
	action.perform()
	测试案例一：
	    打开页面（http://sahitest.com/demo/clicks.htm）
		分别对按钮'click me'，'dbl click me'，'right click me',执行点击，双击，右键操作
		打印上面展示框中的内容
5、ActionChains用法2
    用法二：鼠标移动到某个元素上
	action = ActionChains(self.driver)
	action.move_to_element(element)
	action.perform()
6、表单定义
		表单是一个包含白哦单元素的区域
		表单元素是允许用户在表单中（比如：文本域、下拉列表、单选框、复选框等等），输入信息的元素
		表单使用表单标签（<form>）定义。例如：<form><input/></form>
	操作表单元素步骤：
	    首先要定位到表单元素
		然后去操作元素（清空，输入或者点击等）3.