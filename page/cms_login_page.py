"""
@author:maohui
@time:2022/6/14 16:05
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
import re
import time
from PIL import Image#处理验证码截图的抠图
from PIL import ImageEnhance#修改图片的灰度

import pytesseract#识别抠图的字符串
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class CmsLoginPage():
    def __init__(self,driver):
        #页面元素
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)
        # self.driver=webdriver.Chrome()
        self.name_input_loc=(By.NAME,"txtLoginUser")
        self.pwd_loc=(By.NAME,"txtLoginPwd")
        self.autocode_input_loc=(By.NAME,"txtLoginCode")
        self.autocode_loc=(By.ID,"codeImg")
        self.submit_btn_loc=(By.NAME,"LoginBtn")
    #操作
    def name_input(self):#输入用户名
        self.wait.until(expected_conditions.presence_of_element_located(self.name_input_loc))
        self.driver.find_element(*self.name_input_loc).send_keys("admin")
    def pwd_input(self):#输入密码
        self.wait.until(expected_conditions.presence_of_element_located(self.pwd_loc))
        self.driver.find_element(*self.pwd_loc).send_keys("123456")
    def authcode_input(self):#输入验证码
        self.wait.until(expected_conditions.presence_of_element_located(self.autocode_input_loc))
        #保存截图
        self.driver.get_screenshot_as_file("../authcode_picture/autocode_big.png")
        #左右顶点的坐标轴
        left=self.driver.find_element(*self.autocode_loc).location['x']
        top=self.driver.find_element(*self.autocode_loc).location['y']
        right=self.driver.find_element(*self.autocode_loc).size['width']+left
        height=self.driver.find_element(*self.autocode_loc).size['height']+top
        #抠图后保存
        im=Image.open("../authcode_picture/autocode_big.png")
        img=im.crop((left,top,right,height))
        img.save("../authcode_picture/autocode_true.png")
        #识别抠图后的字符串
        image=Image.open("../authcode_picture/autocode_true.png")
        str_img=pytesseract.image_to_string(image)
        str_input=str_img.replace(" ","")#删除字符串的空格
        print(str_input)
        self.driver.find_element(*self.autocode_input_loc).send_keys(str_input)

    def submit_btn(self):#点击登录
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.submit_btn_loc))
            self.driver.find_element(*self.submit_btn_loc).click()
        except Exception as e:
            raise e

# if __name__=="__main__":
#         driver=webdriver.Chrome()
#         driver.get("http://well-healthcare.com/EN/CMS/Login.aspx")
#         driver.maximize_window()
#         CmsLoginPage=CmsLoginPage(driver)
#         CmsLoginPage.name_input()
#         CmsLoginPage.pwd_input()
#         CmsLoginPage.authcode_input()
#         time.sleep(2)
#         driver.quit()