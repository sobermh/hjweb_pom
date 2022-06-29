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
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from page.index_page import IndexPage
from page.cms_login_page import CmsLoginPage
from page.cms_index_admin_page import CmsIndexAdminPage

class CmsIndexAdmin1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.cmsLoginPage = CmsLoginPage(cls.driver)
        cls.cmsIndexAdminpage = CmsIndexAdminPage(cls.driver)
        cls.indexpage = IndexPage(cls.driver)
    def setUp(self) -> None:
        self.driver.get("http://well-healthcare.com/CMS/Login.aspx")
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
        self.driver.switch_to.alert.accept()
        time.sleep(1)
    def test32(self):
        """后台排序更改，前台显示更改"""
        self.cmsIndexAdminpage.index_admin_click()
        self.cmsIndexAdminpage.index_banner_click()
        self.driver.switch_to.frame('iframe11')
        input=self.wait.until(expected_conditions.presence_of_element_located(self.cmsIndexAdminpage.index_first_sort_loc))
        self.driver.find_element(*self.cmsIndexAdminpage.index_first_sort_loc).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element(*self.cmsIndexAdminpage.index_first_sort_loc).send_keys("100")
        self.driver.find_element(*self.cmsIndexAdminpage.index_first_sort_loc).send_keys(Keys.ENTER)
        #验证
        driver_assert = webdriver.Chrome()
        driver_assert.maximize_window()
        driver_assert.get("http://well-healthcare.com/")
        except_loc = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div/div/div/div[2]')
        wait_assert = WebDriverWait(driver_assert, 15)
        wait_assert.until(
            expected_conditions.presence_of_element_located((except_loc)))
        real=driver_assert.find_element(*except_loc).text
        self.assertEqual("成为普惠化精准医疗的领导者", real)
        driver_assert.quit()
        # 还原内容
        input = self.wait.until(
            expected_conditions.presence_of_element_located(self.cmsIndexAdminpage.index_second_sort_loc))
        self.driver.find_element(*self.cmsIndexAdminpage.index_second_sort_loc).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element(*self.cmsIndexAdminpage.index_second_sort_loc).send_keys("1")
        self.driver.find_element(*self.cmsIndexAdminpage.index_second_sort_loc).send_keys(Keys.ENTER)
    def test33(self):
        """后台首页管理添加信息按钮"""
        self.cmsIndexAdminpage.index_admin_click()
        self.cmsIndexAdminpage.index_banner_click()
        self.driver.switch_to.frame('iframe11')
        self.wait.until(
            expected_conditions.presence_of_element_located(self.cmsIndexAdminpage.index_addmsg_btn_loc))
        self.driver.find_element(*self.cmsIndexAdminpage.index_addmsg_btn_loc).click()

        describe_input=self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="txtTitle2"]')))
        self.driver.find_element(*(By.XPATH,'//*[@id="txtTitle2"]')).send_keys("test")
        self.driver.find_element(*(By.XPATH,'//*[@id="LinkButton1"]/span')).click()
        self.driver.switch_to.alert.accept()
        #验证
        driver_assert = webdriver.Chrome()
        driver_assert.maximize_window()
        driver_assert.get("http://well-healthcare.com/")
        except_loc = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[1]/div/div/div/div[2]')
        wait_assert = WebDriverWait(driver_assert, 15)
        wait_assert.until(
            expected_conditions.presence_of_element_located(except_loc))
        real = driver_assert.find_element(*except_loc).get_attribute('innerHTML')
        print(real)
        self.assertEqual("test", real)
        driver_assert.quit()
        # 还原内容
        del_btn = self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="listPanel"]/div/div/div[2]/div[3]/table/tbody/tr[3]/td[6]/div/div[2]/a')))
        # self.driver.find_element(*(By.XPATH,'//*[@id="listPanel"]/div/div/div[2]/div[3]/table/tbody/tr[3]/td[6]/div/div[2]/a')).click()
        self.driver.execute_script("arguments[0].click();", del_btn)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
    def test34(self):
        """后台首页管理搜索按钮"""
        self.cmsIndexAdminpage.index_admin_click()
        self.cmsIndexAdminpage.index_banner_click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('iframe11')
        self.wait.until(
            expected_conditions.presence_of_element_located(self.cmsIndexAdminpage.index_search_input_loc))
        self.driver.find_element(*self.cmsIndexAdminpage.index_search_input_loc).send_keys("普惠化")
        self.driver.find_element(*self.cmsIndexAdminpage.index_search_btn_loc).click()
        time.sleep(1)
        self.driver.get_screenshot_as_file(f"../log/后台首页管理搜索功能{time.strftime('%Y-%m-%H',time.localtime())}.png")
        # describe_loc=(By.LINK_TEXT,'成为普惠化精准医疗的领导者')
        # expect=self.driver.find_element(*describe_loc).text
        # self.assertIn('普惠化',expect)
    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
