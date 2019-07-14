# -*- coding: utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.billManagePage import BillMPage

class TestBillMPange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test1_query(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.login('admin','admin')

        mainPage = MainPage(driver)
        mainPage.click_zdgl()

        billMpage = BillMPage(driver)
        billMpage.query_by_month_address('2019-01','109-0311')
        billMpage.sleep(5)

    def test2_count_fee(self):
        driver = self.driver
        billMpage = BillMPage(driver)
        sum_fee = billMpage.select_checkbox_items_sum_payFee()
        countFee = billMpage.get_count_fee()
        self.assertEqual(sum_fee,countFee)

    def test3_pay_fee(self):
        driver = self.driver
        billMpage = BillMPage(driver)
        billMpage.do_payFee('浙江绿城建筑科技','20190714111','18667027333')
        billMpage.close_prompt()

if __name__ == '__main__':
    unittest.main()
