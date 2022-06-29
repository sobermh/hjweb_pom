"""
@author:maohui
@time:2022/6/9 16:37
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page.base_keywords_page import BaseKeywordsPage

class AboutPage():
    def __init__(self,driver):
        #页面元素
        self.hj_intro_loc=(By.XPATH,"/html/body/div[4]/div/div/div/a[1]")#汇健简介
        self.hj_develop_loc=(By.XPATH,"/html/body/div[4]/div/div/div/a[2]")#汇健发展
        self.hj_honor_loc=(By.XPATH,"/html/body/div[4]/div/div/div/a[3]")#汇健荣誉
        self.driver = driver
        # self.driver=webdriver.Chrome()#调试
        self.wait = WebDriverWait(self.driver, 20)
        self.baseKeywordsPage=BaseKeywordsPage(self.driver)
    #页面操作
    ##点击汇健简介
    def click_hj_intro(self):
        try:
            time.sleep(2)
            self.baseKeywordsPage.element_presence(self.hj_intro_loc)
            self.baseKeywordsPage.element_click(self.hj_intro_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/点击汇健简介跳转错误.png')
    ##点击汇健发展
    def click_hj_develop(self):
        try:
            self.baseKeywordsPage.element_presence(self.hj_develop_loc)
            self.baseKeywordsPage.element_click(self.hj_develop_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/点击汇健发展跳转错误.png')
    ##点击汇健荣誉
    def click_hj_honor(self):
        try:
            self.baseKeywordsPage.element_presence(self.hj_honor_loc)
            self.baseKeywordsPage.element_click(self.hj_honor_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/点击汇健荣誉跳转错误.png')

# # # 调试
# if __name__ == "__main__":
#     # 打开浏览器
#     driver = webdriver.Chrome()
#     # 最大化窗口
#     driver.maximize_window()
#     index = AboutPage(driver)
#     driver.get("http://47.110.240.87:80/")
#     index.click_hj_intro()
#     driver.quit()
