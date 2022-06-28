"""
@author:maohui
@time:2022/6/28 15:35
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
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from page.index_page import IndexPage


class CaseIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.wait=WebDriverWait(cls.driver,10)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def setUp(self) -> None:
        self.driver.get('http://well-healthcare.com/')
        self.indexpage = IndexPage(self.driver)
    def test25(self):
        """首页汇健科技播放视频功能"""
        hj_loc=self.indexpage.wait.until(expected_conditions.presence_of_element_located(self.indexpage.hj_loc))
        self.driver.execute_script("arguments[0].click();",hj_loc)
        time.sleep(3)
        self.driver.get_screenshot_as_file(f"../log/视频播放截图{time.strftime('%Y-%m-%d-%H', time.localtime())}.png")
    def test26(self):
        """首页跳转公司新闻"""
        company_news_loc=self.wait.until(expected_conditions.presence_of_element_located(self.indexpage.company_news_loc))
        self.driver.execute_script("arguments[0].click();",company_news_loc)
        self.assertEqual(self.driver.current_url,"http://well-healthcare.com/news_40.html")
    def test27(self):
        """点击公司新闻最新之一的竖图跳转"""
        news1_pic_loc = self.wait.until(
            expected_conditions.presence_of_element_located(self.indexpage.news1_pic_loc))
        self.driver.execute_script("arguments[0].click();", news1_pic_loc)
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/news_cont_40_2022_83.html")
    def test28(self):
        """底部的电话正确显示"""
        real=self.driver.find_element(*(By.XPATH,'/html/body/div[8]/div/div/div[1]/div[1]/a')).text
        self.assertEqual(real,'0571-86896257')
    def test29(self):
        """底部导航跳转到汇健发展"""
        hj_dev_loc = self.wait.until(
            expected_conditions.presence_of_element_located(self.indexpage.hj_dev_loc))
        self.driver.execute_script("arguments[0].click();", hj_dev_loc)
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/about.html#d3")
    def test30(self):
        """底部导航跳转到芯片"""
        kit_loc = self.wait.until(
            expected_conditions.presence_of_element_located(self.indexpage.kit_loc))
        self.driver.execute_script("arguments[0].click();", kit_loc)
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/products_list_49.html")
    def test31(self):
        """底部导航跳转到招聘信息"""
        join_msg_loc = self.wait.until(
            expected_conditions.presence_of_element_located(self.indexpage.join_msg_loc))
        self.driver.execute_script("arguments[0].click();", join_msg_loc)
        self.assertEqual(self.driver.current_url, "http://well-healthcare.com/join.html#d3")