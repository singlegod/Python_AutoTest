import os
import time


import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.feature('百度搜索模块测试')
class TestBaiduSearch:
    def get_dir(self):
        """
        获取当前项目地址
        :return:
        """
        now_dir = os.getcwd()
        while True:
            now_dir = os.path.split(now_dir)
            if now_dir[1] == 'test_baidu_search_nogit':
                now_dir = os.path.join(now_dir[0], 'test_baidu_search_nogit')
                break
            now_dir = now_dir[0]
        return now_dir

    def setup(self):
        """前置动作"""
        # driver_path = os.path.join(self.get_dir(),'plugin/windows/chromedriver.exe') # Windows下使用
        driver_path = os.path.join(self.get_dir(), 'plugin/linux/chromedriver') # linux下使用
        option = Options()
        option.add_argument("--headless") # linux下使用无头浏览器需要添加这个参数
        option.add_argument("--no-sandbox") # 表示不用跟用户运行chrome
        option.add_argument("--disable-dev-shm-usage") #防止浏览器异常，不启动
        self.driver = webdriver.Chrome(executable_path=driver_path,chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        """后置动作"""
        self.driver.quit()


    @allure.story('百度搜索测试用例')
    @pytest.mark.parametrize("name", [("狗"), ("猫"), ("zhangsan")])
    def test_baidu_search(self, name):
        self.driver.get("https://www.baidu.com/")
        time.sleep(5)
        self.driver.find_element(By.ID, "kw").send_keys(f"{name}")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(5)
        r = self.driver.title
        assert r == f"{name}_百度搜索"