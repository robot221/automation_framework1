# -*- coding:utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.payInfoReportPage import PayReportPage

class TestPayReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_quesyResults(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin','admin')

        mainpage = MainPage(driver)
        mainpage.click_jfxxbb()

        payReportpage = PayReportPage(driver)
        num = payReportpage.query_and_gettotalnum(custNameOrPhone='15088887777',address='109-1201',startTime='2019-01-01',endTime='2019-02-01')
        self.assertEqual(num,'4')
        owner_phone = payReportpage.view_detail()
        self.assertEqual(owner_phone,'15088887777')
        # L = payReportpage.get_query_results()
        # for l in L:
        #     print(l)

if __name__ == '__main__':
    unittest.main()