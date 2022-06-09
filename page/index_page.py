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
    def __init__(self, driver):
        # 页面元素
        self.search_loc = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]")  # 搜索定位符
        self.search_input_loc = (By.XPATH, "//*[@id='Keywords2']")  # 搜索输入定位符
        self.search_input_btn_loc = (By.XPATH, "// *[ @ id = 'so_btn2'] / a")  # 点击搜索按钮定位符
        self.menu_loc = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]")  # 菜单定位符
        self.about_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[2]/a")  # 关于汇健定位符
        self.platform_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[3]/a")  # 技术平台定位符
        self.product_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[4]/a")  # 产品中心定位符
        self.cooperation_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[5]/a")  # 医学合作定位符
        self.news_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[8]/a")  # 新闻中心定位符
        self.hj_loc = (By.XPATH, "/html/body/div[5]/div/ul/li[1]/div[2]/div[4]/img")  # 汇健科技视频定位符
        self.company_news_loc = (By.XPATH, "/html/body/div[6]/div/a/span")  # 公司新闻定位符
        self.driver = driver
        # self.driver=webdriver.Chrome()#调试
        self.wait = WebDriverWait(self.driver, 90)

    #点击搜索
    def tosearch(self):
        try:
            time.sleep(2)
            self.wait.until(expected_conditions.presence_of_element_located(self.search_loc))
            self.driver.find_element(*self.search_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/点击搜索错误.png')
            raise e
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.search_input_loc))
            time.sleep(2)
            self.driver.find_element(*self.search_input_loc).send_keys("汇健")
            self.driver.find_element(*self.search_input_btn_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/搜索错误.png')
            raise e
    # 点击menu
    def click_menu(self):
        try:
            time.sleep(2)
            self.wait.until(expected_conditions.presence_of_element_located(self.menu_loc))
            self.driver.find_element(*self.menu_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/打开menu错误.png')
            raise e
    #点击关于汇健
    def click_about(self):
        try:
            time.sleep(2)
            self.wait.until(expected_conditions.presence_of_element_located(self.about_loc))
            self.driver.find_element(*self.about_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/打开about错误.png')
            raise e
    # 点击新闻中心
    def click_news(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.news_loc))
            self.driver.find_element(*self.news_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file("./log/打开新闻错误.png")
            raise e


# # 调试
# if __name__ == "__main__":
#     # 打开浏览器
#     driver = webdriver.Chrome()
#     # 最大化窗口
#     driver.maximize_window()
#     index = IndexPage(driver)
#     driver.get("http://47.110.240.87:80/")
#     index.tosearch()
#     driver.quit()

