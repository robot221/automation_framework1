# -*- coding:utf-8 -*-
from configparser import ConfigParser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlogger()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('..'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        config = ConfigParser()
        file_path = self.dir + '/config/config.ini'
        config.read(file_path,encoding='utf-8')
        browser = config.get("browserType","browserName")
        logger.info(f'你选择的浏览器是 {browser}')
        url = config.get("testServer","URL")
        logger.info(f'待测试系统的URL是：{url}')

        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info('开始启动火狐浏览器')
        elif browser == 'Chrome':
            options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
            options.add_experimental_option('prefs', prefs)
            driver = webdriver.Chrome(self.chrome_driver_path,options=options)
            logger.info('开始启动谷歌浏览器')

        driver.get(url)
        logger.info(f'打开的URL是：{url}')
        driver.maximize_window()
        logger.info('最大化当前窗口')
        driver.implicitly_wait(10)
        logger.info('设置隐式等待时间为10秒')
        return driver

    def quit_browser(self):
        logger.info('现在，关闭并退出浏览器')
        self.driver.quit()

