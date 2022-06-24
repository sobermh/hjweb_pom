"""
@author:maohui
@time:2022/6/24 10:19
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
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page.index_page import IndexPage
from page.cms_login_page import CmsLoginPage
from page.cms_index_admin_page import CmsIndexAdmin

class CmsIndexAdmin1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)
        self.cmsLoginPage = CmsLoginPage(self.driver)
        self.cmsIndexAdminpage = CmsIndexAdmin(self.driver)
        self.indexpage = IndexPage(self.driver)
        self.driver.get("http://well-healthcare.com/CMS/Index.aspx")
        self.cmsLoginPage.name_input("admin")
        self.cmsLoginPage.pwd_input("123456")
        self.cmsLoginPage.authcode_input()
        self.cmsLoginPage.submit_btn()
    def test014(self):
        """后台修改首页汇健科技的了解更多跳转链接，前台点击了解更多跳转链接更换"""
        self.cmsIndexAdminpage.index_admin_click()
        # time.sleep(2)
        self.cmsIndexAdminpage.index_content_click()
        self.driver.switch_to.frame('iframe12')
        self.wait.until(expected_conditions.presence_of_element_located((By.NAME, 'txtTitle3')))
        self.driver.find_element(*(By.NAME, 'txtTitle3')).clear()
        self.driver.find_element(*(By.NAME, 'txtTitle3')).send_keys('http://www.baidu.com/')
        self.driver.find_element(*(By.XPATH, '//*[@id="LinkButton1"]/span')).click()
        self.driver.switch_to.alert.accept()
        # 验证
        driver_assert = webdriver.Chrome()
        driver_assert.get("http://47.110.240.87:80/")
        except_loc = (By.XPATH, '/html/body/div[5]/div/ul/li[1]/div[2]/div[4]/img')
        wait_assert = WebDriverWait(driver_assert, 15)
        wait_assert.until(
            expected_conditions.presence_of_element_located((except_loc)))
        driver_assert.find_element(*except_loc).click()
        driver_assert.find_element(*(By.XPATH, '/html/body/div[7]/div/a')).click()
        self.assertEqual(driver_assert.current_url, "https://www.baidu.com/")
        driver_assert.quit()
        #还原内容
        self.driver.find_element(*(By.NAME, 'txtTitle3')).clear()
        self.driver.find_element(*(By.NAME, 'txtTitle3')).send_keys('http://www.well-healthcare.com/about.html')
        self.driver.find_element(*(By.XPATH, '//*[@id="LinkButton1"]/span')).click()
    def tearDown(self) -> None:
        self.driver.quit()
    @classmethod
    def tearDownClass(cls) -> None:
        pass
