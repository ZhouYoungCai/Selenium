1、使用selenium直接在当前页面进行js交互
   常用的几种操作js实现
2、js的处理
    selenium能够执行js，这使得selenium拥有更为强大的能力。既然能执行js，那么js能做的事，selenium应该大部分也能做
	直接使用js操作页面，能解决很多click()不生效的问题
	页面滚动到底部，顶部
	处理富文本，时间控件的输入
3、selenium中如何调用js
    例如js代码：
	   window.alert('selenium弹框测试')
	   a = document.getElementById('KW').value
	   document.title
	   JSON.stringify(performance.timing)
	execute_script:执行js
	return：可以返回js的返回结果
	execute_script:arguments传参
4、js处理-案例3-时间控件
    大部分时间控件都是readonly属性，需要手动去选择对应的时间，手工测试中很容易做到，
	自动化中对控件的操作可以使用js来操作。
	处理时间控件思路：
	    1、要取消日期的readonly属性
		2、给value赋值
		写js代码来实现如上的1/2点，再webdriver对js进行处理
5、