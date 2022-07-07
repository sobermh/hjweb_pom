"""
@author:maohui
@time:2022/6/9 17:07
"""
import time

from selenium import webdriver
from page.about_page import AboutPage
from page.index_page import IndexPage
import unittest

class IndexToPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def setUp(self) -> None:
        self.driver.get("http://well-healthcare.com/")
        self.indexpage=IndexPage(self.driver)
        self.hjintro=AboutPage(self.driver)
    def test002(self):
        """首页跳转至关于汇健"""
        self.indexpage.click_menu()
        self.indexpage.click_about()
        self.assertEqual(self.driver.current_url,"http://well-healthcare.com/about.html")
    def test003(self):
        """首页跳转至技术平台"""
        self.indexpage.click_menu()
        self.indexpage.click_platform()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/platform.html")
    def test004(self):
        """首页跳转至产品中心"""
        self.indexpage.click_menu()
        self.indexpage.click_product()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/products.html")
    def test005(self):
        """首页跳转至医学合作中心"""
        self.indexpage.click_menu()
        self.indexpage.click_cooperate()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/cooperate.html")
    def test006(self):
        """首页跳转至医学检验中心"""
        self.indexpage.click_menu()
        self.indexpage.click_test()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/test.html")
    def test007(self):
        """首页跳转至呼气传感中心"""
        self.indexpage.click_menu()
        self.indexpage.click_sensing()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/sensing.html")
    def test008(self):
        """首页跳转至新闻中心"""
        self.indexpage.click_menu()
        self.indexpage.click_news()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/news.html")
    def test009(self):
        """首页跳转至新闻中心"""
        self.indexpage.click_menu()
        self.indexpage.click_join()
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/join.html")
