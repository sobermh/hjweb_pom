"""
@author:maohui
@time:2022/6/23 16:28
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
class CmsIndexAdmin():
    # 页面元素
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)
        # self.driver=webdriver.Chrome()
        self.index_admin_loc=(By.XPATH,'//*[@id="wrapper"]/div[1]/div/div[2]/ul/li[3]/a/div/span')#首页管理
        self.index_banner_loc=(By.XPATH,"//*[@id='wrapper']/div[1]/div/div[2]/ul/li[3]/ul/li[1]/a")#首页banner
        self.index_content_loc = (By.XPATH, '//*[@id="wrapper"]/div[1]/div/div[2]/ul/li[3]/ul/li[2]/a')  # 首页banner
    #操作
    #点击首页管理
    def index_admin_click(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.index_admin_loc))
        self.driver.find_element(*self.index_admin_loc).click()
    #点击首页banner
    def index_banner_click(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.index_banner_loc))
        self.driver.find_element(*self.index_banner_loc).click()
    #点击首页内容
    def index_content_click(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.index_content_loc))
        self.driver.find_element(*self.index_content_loc).click()
# if __name__=="__main__":
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://www.well-healthcare.com/CMS/Index.aspx")
#     cmsIndexAdmin=CmsIndexAdmin(driver)
#     cmsIndexAdmin.index_admin_click()