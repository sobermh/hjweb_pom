"""
@author:maohui
@time:2022/4/21 13:30
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class IndexPage():
    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()#调试
        self.wait=WebDriverWait(driver,90)
    #点击menu
    def click_menu(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/ul")))
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/ul').click()
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/打开menu错误.png')
            raise e
    #点击新闻中心
    def click_news(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[2]/a")))
            self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[2]/a").click()
        except Exception as e:
            self.driver.get_screenshot_as_file("./log/打开新闻错误.png")
            raise e


#调试
if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://47.110.240.87:10001/")

    index_page=IndexPage(driver)
    index_page.click_menu()
    time.sleep(1)
    index_page.click_news()
    time.sleep(1)

    driver.quit()