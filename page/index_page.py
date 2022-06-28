"""
/**
 * 　　　　　　　 ┏┓    ┏┓+ +
 * 　　　　　　　┏┛┻━━━━┛┻┓ + +
 * 　　　　　　　┃        ┃ 　
 * 　　　　　　　┃     ━  ┃ ++ + + +
 * 　　　　　 　████━████ ┃+
 * 　　　　　　　┃        ┃ +
 * 　　　　　　　┃   ┻    ┃
 * 　　　　　　　┃        ┃ + +
 * 　　　　　　　┗━┓   ┏━━┛
 * 　　　　　　　  ┃   ┃
 * 　　　　　　　  ┃   ┃ + + + +
 * 　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
 * 　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
 * 　　　　　　　  ┃   ┃
 * 　　　　　　　  ┃   ┃　　+
 * 　　　　　　　  ┃   ┗━━━━━━━┓ + +
 * 　　　　　　　  ┃           ┣┓
 * 　　　　　　　  ┃           ┏┛
 * 　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
 * 　　　　　　　   ┃┫┫     ┃┫┫
 * 　　　　　　　   ┗┻┛     ┗┻┛+ + + +
 */
"""
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
        self.cooperate_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[5]/a")  # 医学合作定位符
        self.test_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[6]/a")  # 医学检验定位符
        self.sensing_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[7]/a")  # 呼气传感定位符
        self.news_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[8]/a")  # 新闻中心定位符
        self.join_loc = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[9]/a")  # 加入汇健定位符

        self.hj_loc = (By.XPATH, "/html/body/div[5]/div/ul/li[1]/div[2]/div[4]/img")  # 汇健科技视频定位符
        self.company_news_loc = (By.XPATH, "/html/body/div[6]/div/a/span")  # 公司新闻定位符
        self.news1_pic_loc = (By.XPATH,'/html/body/div[6]/div/ul/li[1]/a/div[1]/s')#第一张公司新闻图

        self.hj_dev_loc=(By.XPATH,'/html/body/div[8]/div/div/div[2]/ul/li[1]/div[2]/a[2]') # 汇健发展
        self.kit_loc=(By.XPATH,'/html/body/div[8]/div/div/div[2]/ul/li[3]/div[2]/a[3]') # 试剂盒
        self.join_msg_loc=(By.XPATH,'/html/body/div[8]/div/div/div[2]/ul/li[8]/div[2]/a[3]') # 招聘信息




        self.driver = driver
        # self.driver=webdriver.Chrome()#调试
        self.wait = WebDriverWait(self.driver, 20)
    #时间
    def st(self):
        st = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        st='../screenshot/'+st
        return st
    # 点击搜索
    def tosearch(self):
        try:
            # time.sleep(2)
            search_loc = self.wait.until(expected_conditions.presence_of_element_located(self.search_loc))
            self.driver.execute_script("arguments[0].click();", search_loc)
            # self.driver.find_element(*self.search_loc).click() 无法点击 元素被覆盖
        except Exception as e:
            filename = self.st() + '点击搜索错误.png'
            # path = os.path.abspath('screenshot')
            self.driver.get_screenshot_as_file(filename)
            raise e
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(self.search_input_loc))
            # time.sleep(2)
            self.driver.find_element(*self.search_input_loc).send_keys("汇健")
            search_input_btn_lo = self.wait.until(
                expected_conditions.element_to_be_clickable(self.search_input_btn_loc))
            self.driver.execute_script("arguments[0].click();", search_input_btn_lo)
            # self.driver.find_element(*self.search_input_btn_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/搜索错误.png')
            raise e
    # 点击menu
    def click_menu(self):
        try:
            time.sleep(2)
            self.wait.until(expected_conditions.presence_of_element_located(self.menu_loc))
            self.driver.find_element(*self.menu_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/打开menu错误.png')
            raise e

    # 点击关于汇健
    def click_about(self):
        try:
            # time.sleep(2)
            about_loc=self.wait.until(expected_conditions.presence_of_element_located(self.about_loc))
            # self.driver.find_element(*self.about_loc).click()
            self.driver.execute_script("arguments[0].click();", about_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('./log/打开about错误.png')
            raise e

    # 点击技术平台
    def click_platform(self):
        try:
            platform_loc=self.wait.until(expected_conditions.presence_of_element_located(self.platform_loc))
            self.driver.execute_script("arguments[0].click();",platform_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/打开关于汇健错误.png')
            raise e

    #点击产品中心
    def click_product(self):
        try:
            product_loc=self.wait.until(expected_conditions.presence_of_element_located(self.product_loc))
            self.driver.execute_script("arguments[0].click();",product_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/打开产品中心错误.png')
            raise e

    #点击医学合作
    def click_cooperate(self):
        try:
            cooperate_loc=self.wait.until(expected_conditions.presence_of_element_located(self.cooperate_loc))
            self.driver.execute_script("arguments[0].click();",cooperate_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/打开医学合作错误.png')
            raise e

    #点击医学检验
    def click_test(self):
        try:
            test_loc=self.wait.until(expected_conditions.presence_of_element_located(self.test_loc))
            self.driver.execute_script("arguments[0].click()",test_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/打开医学检验错误.png')
            raise e

    #点击呼气传感
    def click_sensing(self):
        try:
            sensing_loc=self.wait.until(expected_conditions.presence_of_element_located(self.sensing_loc))
            self.driver.execute_script("arguments[0].click();",sensing_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file('../log/打开呼气传感错误.png')
            raise e

    # 点击新闻中心
    def click_news(self):
        try:
            # time.sleep(1)
            news_loc=self.wait.until(expected_conditions.presence_of_element_located(self.news_loc))
            # self.driver.find_element(*self.news_loc).click()
            self.driver.execute_script("arguments[0].click();",news_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file("../log/打开新闻错误.png")
            raise e

    # 点击加入汇健
    def click_join(self):
        try:
            join_loc=self.wait.until(expected_conditions.presence_of_element_located(self.join_loc))
            self.driver.execute_script("arguments[0].click();",join_loc)
        except Exception as e:
            self.driver.get_screenshot_as_file("../log/打开加入汇健错误.png")
            raise e


# 调试
if __name__ == "__main__":
    # 打开浏览器
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    index = IndexPage(driver)
    driver.get("http://47.110.240.87:80/")
    wait=WebDriverWait(driver,15)
    except_loc = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div/div/div/div[2]')
    wait.until(
        expected_conditions.presence_of_element_located((except_loc)))
    print(driver.find_element(*except_loc).text)
    time.sleep(2)
    driver.quit()
