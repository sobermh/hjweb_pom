"""
@author:maohui
@time:2022/6/24 11:05
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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CmsAboutHjPage():
    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()
        self.wait=WebDriverWait(self.driver,15)
        self.about_hj_banner_loc=(By.XPATH,'//*[@id="wrapper"]/div[1]/div/div[2]/ul/li[4]/ul/li[1]/a')
        self.about_hj_loc=(By.XPATH,'//*[@id="wrapper"]/div[1]/div/div[2]/ul/li[4]/a/div/span')
    #点击关于汇健
    def about_hj_click(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.about_hj_loc))
        self.driver.find_element(*(self.about_hj_loc)).click()
    #点击关于汇健banner
    def about_hj_banner_click(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.about_hj_banner_loc))
        self.driver.find_element(*(self.about_hj_banner_loc)).click()
# if __name__=="__main__":
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://www.well-healthcare.com/CMS/Index.aspx")
#     cmsIndexAdmin=CmsIndexAdmin(driver)
#     cmsIndexAdmin.index_admin_click()
