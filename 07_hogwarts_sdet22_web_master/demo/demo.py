"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


class WeworkPage:
    _Base_URL = "父类属性"
    def print_demo(self):
        print(self._Base_URL)

class MainPageObject(WeworkPage):
    _Base_URL = "子类属性"



if __name__ == '__main__':
    # demo = Demo()
    # demo.print_demo()
    main_demo = MainPageObject()
    main_demo.print_demo()