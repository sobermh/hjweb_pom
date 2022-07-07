"""
@author:maohui
@time:2022/6/9 15:57
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page.index_page import IndexPage


class Search(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     # 打开浏览器
    #     cls.driver = webdriver.Chrome()
    #     # 最大化窗口
    #     cls.driver.maximize_window()
    #     # 加载网页
    #     # cls.driver.get("http://47.110.240.87:80/")

    def setUp(self) -> None:
        # 打开浏览器
        self.driver=webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 加载网页
        self.driver.get("http://47.110.240.87:80/")
        self.index = IndexPage(self.driver)

    def test001(self):
        """ 正常搜索功能"""
        # 点击搜索并输入搜索内容
        self.index.tosearch()
        time.sleep(1)
        ele=self.driver.find_element(By.ID,"Keywords3")
        self.assertEqual(self.driver.current_url,"http://47.110.240.87/search.html?key=%E6%B1%87%E5%81%A5#d1")
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main":
    unittest.main()