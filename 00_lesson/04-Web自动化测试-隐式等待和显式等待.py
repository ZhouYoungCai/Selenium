1、selenium的三种等待方式
    直接等待
	隐式等待
	显示等待
2、直接等待
    强制等待，线程休眠一定时间
	用法：
	      import time            time.sleep(2)
	      from time import *     sleep(2)
3、隐式等待 
    设置一个等待时间，轮询查找（默认0.5秒）元素是否出现
	如果没有出现就抛出异常
	用法：self.driver.implicitly_wait(2)
    全局的等待
4、显示等待
    在代码定义等待条件，当条件发生时才继续执行代码
	“WebDriverWait”配合until()和until_not()方法，根据判断条件进行等待
	程序每隔一段时间（默认0.5秒）进行条件判断
	如果条件成立，则执行下一步
	否则继续等待，直到超过设置的最长时间
	