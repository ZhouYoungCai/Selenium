1、文件上传
    input标签可以直接使用send_keys(文件地址)上传文件
	用法：
	     el = driver.find_element_by_id('上传按钮id')
	     el.send_keys("文件路径+文件名")
2、弹框处理机制
    操作alert常用的方法：
	    switch_to.alert():获取当前页面上的警告框
		text： 返回alert/confirm/prompt中的文字信息
		accept()：接受现有警告框
		dissmiss():解散现有警告框
		send_keys(keysToSend):发送文本至警告框。keysToSend：将文本发送至警告框