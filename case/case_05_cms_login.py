"""
@author:maohui
@time:2022/6/23 11:59
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from page.cms_login_page import CmsLoginPage
from page.cms_index_admin_page import CmsIndexAdminPage
from page.index_page import IndexPage
from selenium import webdriver




class CmsLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器
        cls.driver = webdriver.Chrome()
        cls.wait=WebDriverWait(cls.driver,15)
        # 加载网页
        cls.driver.maximize_window()
        cls.driver.get("http://well-healthcare.com/CMS/Login.aspx")

        # 实例化登录页面类，并正确登录
        cls.cmsLoginPage=CmsLoginPage(cls.driver)
        cls.cmsIndexAdminpage=CmsIndexAdminPage(cls.driver)
        cls.indexpage = IndexPage(cls.driver)
        cls.cmsLoginPage.name_input("admin")
        cls.cmsLoginPage.pwd_input("123456")
        cls.cmsLoginPage.authcode_input()
        cls.cmsLoginPage.submit_btn()
    def test012(self):
        """正确登录成功"""
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/CMS/Index.aspx")
        time.sleep(2)
    def test013(self):
        """后台修改首页banner描述,前台首页banner同步修改"""
        self.cmsIndexAdminpage.index_admin_click()
        self.cmsIndexAdminpage.index_banner_click()
        self.driver.switch_to.frame('iframe11')
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="repInfo_ctl00_LinkButton3"]/span')))
        self.driver.find_element(*(By.XPATH,'//*[@id="repInfo_ctl00_LinkButton3"]/span')).click()
        # self.driver.execute_script("arguments[0].click();",(By.XPATH,"//*[@id='repInfo_ctl00_LinkButton3']/i"))#点击编辑
        self.wait.until(
            expected_conditions.presence_of_element_located(((By.NAME,'txtTitle2'))))
        self.driver.find_element(*(By.NAME,'txtTitle2')).send_keys("test")
        self.driver.find_element(*(By.XPATH,'//*[@id="LinkButton1"]/span')).click()
        #验证
        driver_assert=webdriver.Chrome()
        driver_assert.get("http://47.110.240.87:80/")
        except_loc=(By.XPATH,'/html/body/div[4]/div[1]/div[1]/div[2]/div/div/div/div[2]')
        wait_assert=WebDriverWait(driver_assert,15)
        wait_assert.until(
            expected_conditions.presence_of_element_located((except_loc)))
        expect=driver_assert.find_element(*except_loc).text
        self.assertEqual("创新组学技术 服务人类健康test",expect)
        #恢复
        self.driver.switch_to.alert.accept()
        # self.driver.switch_to.frame('iframe11')
        self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="repInfo_ctl00_LinkButton3"]/span')))
        self.driver.find_element(*(By.XPATH, '//*[@id="repInfo_ctl00_LinkButton3"]/span')).click()
        # self.driver.execute_script("arguments[0].click();",(By.XPATH,"//*[@id='repInfo_ctl00_LinkButton3']/i"))#点击编辑
        self.wait.until(
            expected_conditions.presence_of_element_located(((By.NAME, 'txtTitle2'))))
        self.driver.find_element(*(By.NAME, 'txtTitle2')).clear()
        self.driver.find_element(*(By.NAME, 'txtTitle2')).send_keys("创新组学技术       服务人类健康")
        self.driver.find_element(*(By.XPATH, '//*[@id="LinkButton1"]/span')).click()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        driver_assert.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
