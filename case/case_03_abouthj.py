"""
@author:maohui
@time:2022/6/9 17:07
"""
import time
import unittest
from selenium import webdriver
from page.about_page import AboutPage
from page.index_page import IndexPage
from page.base_keywords_page import BaseKeywordsPage


class HjDevelop(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        # cls.baseKeywordsPage=BaseKeywordsPage(cls.driver)
        cls.indexpage = IndexPage(cls.driver)
        cls.aboutpage = AboutPage(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def setUp(self) -> None:
        self.driver.get("http://47.110.240.87:80/")
    def test010(self):
        """关于汇健中汇健发展的跳转"""
        self.indexpage.click_menu()
        self.indexpage.click_about()
        self.aboutpage.click_hj_develop()
        time.sleep(1)
    def test011(self):
        """关于汇健中汇健荣誉的跳转"""
        self.indexpage.click_menu()
        self.indexpage.click_about()
        self.aboutpage.click_hj_honor()
        time.sleep(1)
    def tearDown(self) -> None:
        pass