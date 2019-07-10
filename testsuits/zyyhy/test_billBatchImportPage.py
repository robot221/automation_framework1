# -*- coding:utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.billBatchImportPage import BillBIPage

class TestBBIPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @unittest.skip('调试，暂不执行')
    def testbatchImport(self):
        '''账单批量导入'''
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin','admin')

        mainpage = MainPage(driver)
        mainpage.click_zdpldr()

        bbiPage = BillBIPage(driver)
        filePath = r'C:\Users\Hi\Downloads\20190709144305-账单模板.xls'
        bbiPage.batchImportBill(filePath)

    def testImportDetail(self):
        '''查看明细'''
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_zdpldr()

        bbiPage = BillBIPage(driver)
        failNum = bbiPage.view_detail_and_get_failNum()
        self.assertEqual(failNum,'0')

if __name__ == '__main__':
    unittest.main()