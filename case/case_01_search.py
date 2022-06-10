"""
@author:maohui
@time:2022/6/9 15:57
"""
import time
import unittest
from selenium import webdriver
from page.index_page import IndexPage

class Search(unittest.TestCase):
    def setUp(self) -> None:
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        self.index = IndexPage(self.driver)
    def test001(self):
        # 加载网页
        self.driver.get("http://47.110.240.87:80/")
        #点击搜索并输入搜索内容
        self.index.tosearch()
        time.sleep(1)
    def tearDown(self) -> None:
        self.driver.quit()