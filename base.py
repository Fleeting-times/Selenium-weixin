import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test():
    def setup(self):
        #初始化Chrome浏览器
        self.driver = webdriver.Chrome()

        # 定义隐式等待
        self.driver.implicitly_wait(5)

        # 定义最大屏幕
        self.driver.maximize_window()


    #获取当前网页的cookies信息
    def test_cookies(self):
        # 访问企业微信
        self.driver.get("https://work.weixin.qq.com/")

        # 点击企业登录
        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()

        # 设置等点时间，用于微信扫码使用
        sleep(5)

        # 点击通讯录，验证能否正常跳转
        self.driver.find_element(By.ID, 'menu_contacts').click()

        # 获取当前网页的cookies
        cookies_dic = self.driver.get_cookies()

        # 去除当前网页cookies中的时间节点字段
        for cookie in cookies_dic:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")

        # 创建或打开一个名为“cookies”的shelve文件
        db = shelve.open("cookies")

        # 将进行处理过的cookies数据存储在shelve文件中
        db['cookies'] = cookies_dic
