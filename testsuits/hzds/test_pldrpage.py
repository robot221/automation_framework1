# -*- coding:utf-8 -*-

import unittest
from pageobjects.hzds.mainpage import MainPage
from pageobjects.hzds.loginpage import LoginPage
from framework.browser_engine import BrowserEngine
from pageobjects.hzds.pldrpage import PldrPage
from pywinauto import application  #Spy++
class TestPldrPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #@unittest.skip('暂时跳过该用例')
    def test_upload(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        mainPage = MainPage(driver)
        pldrPage = PldrPage(driver)

        loginPage.login('admin','admin')
        mainPage.click_xgsjpldr_menu()
        pldrPage.updatefile()
        pldrPage.sleep(3)
        app = application.Application()
        app.connect(title=u'打开',class_name='#32770')
        window = app.window(title=u'打开',class_name='#32770')
        # 文件所在路径不能含有空格
        window["Edit"].type_keys(r"C:\Users\Hi\巡更数据导入模板.xls")
        pldrPage.sleep(3)
        window["ScrollBar"].click()
        window[u"打开(O)"].click()
        pldrPage.sleep(3)

    @unittest.skip('暂时跳过该用例')
    def test_download(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        mainPage = MainPage(driver)
        pldrPage = PldrPage(driver)

        loginPage.login('admin', 'admin')
        mainPage.click_xgsjpldr_menu()
        pldrPage.downloadfile()
        pldrPage.sleep(3)

if __name__ == "__main__":
    unittest.main()