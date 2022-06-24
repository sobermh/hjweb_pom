"""
@author:maohui
@time:2022/6/24 11:04
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from page.cms_about_hj_page import CmsAboutHjPage
from page.cms_login_page import CmsLoginPage
class CmsAboutHj(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.wait=WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.driver.get("http://well-healthcare.com/CMS/Index.aspx")
        self.cmsAboutHjPage=CmsAboutHjPage(self.driver)
        self.cmsLoginPage=CmsLoginPage(self.driver)
        self.cmsLoginPage.name_input("admin")
        self.cmsLoginPage.pwd_input("123456")
        self.cmsLoginPage.authcode_input()
        self.cmsLoginPage.submit_btn()
    def test015(self):
        """后台修改关于汇健banner说明，前台关于汇健banner发生改变"""
        self.cmsAboutHjPage.about_hj_click()
        self.cmsAboutHjPage.about_hj_banner_click()
        self.driver.switch_to.frame("iframe16")
        self.wait.until(expected_conditions.presence_of_element_located((By.NAME, 'txtSummary')))
        self.driver.find_element(*(By.NAME, 'txtSummary')).clear()
        self.driver.find_element(*(By.NAME, 'txtSummary')).send_keys('text')
        self.driver.find_element(*(By.XPATH, '//*[@id="LinkButton1"]/span')).click()
        self.driver.switch_to.alert.accept()
        # 验证
        driver_assert = webdriver.Chrome()
        driver_assert.get("http://www.well-healthcare.com/about.html")
        except_loc = (By.XPATH, '/html/body/div[3]/div/div')
        wait_assert = WebDriverWait(driver_assert, 15)
        wait_assert.until(
            expected_conditions.presence_of_element_located((except_loc)))
        except_text=driver_assert.find_element(*except_loc).text
        self.assertEqual(except_text, "text")
        driver_assert.quit()
        # 还原内容
        self.driver.find_element(*(By.NAME, 'txtSummary')).clear()
        self.driver.find_element(*(By.NAME, 'txtSummary')).send_keys('创新组学诊断技术平台')
        self.driver.find_element(*(By.XPATH, '//*[@id="LinkButton1"]/span')).click()
    def tearDown(self) -> None:
        self.driver.quit()