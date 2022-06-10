"""
@author:maohui
@time:2022/6/9 17:07
"""
# import time
#
# from selenium import webdriver
# from page.about_page import AboutPage
# from page.index_page import IndexPage
# import unittest
#
# class HjHonor(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         self.indexpage=IndexPage(self.driver)
#         self.aboutpage=AboutPage(self.driver)
#     def test004(self):
#         self.driver.get("http://47.110.240.87:80/")
#         self.indexpage.click_menu()
#         self.indexpage.click_about()
#         self.aboutpage.click_hj_honor()
#         time.sleep(1)
#     def tearDown(self) -> None:
#         self.driver.quit()