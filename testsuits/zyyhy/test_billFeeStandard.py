# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.billFeeStandard import BillFeeStandard

class TestBFS(unittest.TestCase):
    '''物业收费标准测试用例'''
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test1_add(self):
        '''新增物业收费标准'''
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.login('admin','admin')
        mainPage = MainPage(driver)
        mainPage.click_wysfbz()

        billFS = BillFeeStandard(driver)
        billFS.add_feeStandard(systemName='明珠国际',feeTypeName='水费',content='水费')
        #billFS.sleep(1)
        billFS.close_alert()
        billFS.sleep(2)

   # @unittest.skip('调试')
    def test2_modify(self):
        '''修改物业收费标准'''
        driver = self.driver
        billFS = BillFeeStandard(driver)
        billFS.modify_feeStandard('明珠国际',content='测试管理费')
        billFS.sleep(1)
        billFS.close_alert()
        billFS.sleep(1)

    def test3_delete(self):
        '''删除物业收费标准'''
        driver = self.driver
        billFS = BillFeeStandard(driver)
        billFS.del_feeStandard('明珠国际')
        billFS.sleep(1)
        billFS.close_alert()

if __name__ == '__main__':
    unittest.main()