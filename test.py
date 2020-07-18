import shelve
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test():
        def setup(self):
                # 初始化Chrome浏览器
                self.driver = webdriver.Chrome()

                # 定义隐式等待
                self.driver.implicitly_wait(5)

                # 定义最大屏幕
                self.driver.maximize_window()


        def test_weixin(self):
                #读取shelve数据
                cookies = shelve.open("cookies")

                #模拟登陆企业微信
                self.driver.get("https://work.weixin.qq.com/")

                #上传cookies信息
                for cookie in cookies["cookies"]:
                        self.driver.add_cookie(cookie)

                self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
                self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
                cookies.close()