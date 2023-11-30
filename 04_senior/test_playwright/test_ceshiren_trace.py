"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from playwright.sync_api import sync_playwright, expect


def test_ceshiren():
    # 实例化一个playwright对象
    playwright = sync_playwright().start()
    # 启动谷歌浏览器，模式使用无头模式
    browser = playwright.chromium.launch(headless=False)
    # =========== trace 的配置
    # 1. 生成 一个 context 实例
    context = browser.new_context()
    # 2. 添加 trace 的配置信息
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # 3. 使用填加了trace 配置的 context 实例，去实例化一个page对象
    page = context.new_page()
    # 跳转到ceshiren页面
    page.goto("https://ceshiren.com/")
    # 点击搜索按钮， 输入css定位
    page.locator("#search-button").click()
    # 输入搜索的内容， 输入css定位
    page.locator("#search-term").fill("Appium")
    # 按下回车键
    page.keyboard.down("Enter")
    # time.sleep(3)
    result = page.locator(".results .item:nth-child(1) .topic-title")
    expect(result).to_contain_text("Appium")
    # 4. 在关闭浏览器之前，一定要结束trace
    context.tracing.stop(path="ceshiren.zip")
    browser.close()
