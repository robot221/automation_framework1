# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.dialRecordPage import DialRecordPage

class TestDialRecordPage(unittest.TestCase):
    """
    拨打记录测试用例
    """

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')
        mainPage = MainPage(driver)
        mainPage.click_bdjl()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_query(self):
        """查询用例"""
        dialRPage = DialRecordPage(self.driver)
        dialRPage.query(propertyName='王先利')
        recordNum = dialRPage.get_totalCount()
        self.assertEqual(recordNum,2)

if __name__ == '__main__':
    unittest.main()
