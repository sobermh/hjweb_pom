"""
@author:maohui
@time:2022/6/24 11:58
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""
import unittest

from ddt import ddt, data, unpack, file_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from page.cms_login_page import CmsLoginPage


@ddt
class CmsFaultLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.driver.maximize_window()
        cls.cmsLoginPage = CmsLoginPage(cls.driver)
    def setUp(self) -> None:
        self.driver.get("http://well-healthcare.com/CMS/Login.aspx")
    @data('admin', 'text', 'maohui')
    def test017(self, name):
        """相同密码，不同账号登录"""
        self.cmsLoginPage.name_input(name)
        self.cmsLoginPage.pwd_input("123456")
        self.cmsLoginPage.authcode_input()
        # self.cmsLoginPage.submit_btn()

    @file_data('../data/login.yaml')
    def test018(self, common,pwd):
        """相同账号，不同密码登录"""
        #如果是多参数用**common，**kwargs
        self.cmsLoginPage.name_input(common['name'])
        self.cmsLoginPage.pwd_input(pwd)
        self.cmsLoginPage.authcode_input()
        # self.cmsLoginPage.submit_btn()

    @data(['admin', '123456'], ['text', '123456'])
    @unpack
    def test019(self, name, pwd):
        """不同账号密码登录"""
        self.cmsLoginPage.name_input(name)
        self.cmsLoginPage.pwd_input(pwd)
        self.cmsLoginPage.authcode_input()
        # self.cmsLoginPage.submit_btn()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
