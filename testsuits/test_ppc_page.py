# -*- coding:utf-8 -*-

import unittest
from pageobjects.hzds.mainpage import MainPage
from pageobjects.hzds.loginpage import LoginPage
from framework.browser_engine import BrowserEngine
from pageobjects.hzds.ppc_page import PPCPage

class TestPPCPage(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        driver = browser.open_browser(self)
        self.driver = driver
    def tearDown(self):
        self.driver.quit()

    def test_seach_po(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        mainPage = MainPage(driver)
        ppcPage = PPCPage(driver)

        loginPage.login('admin', 'admin')
        mainPage.click_xgdfl_menu()
        mainPage.sleep(1)

        self.assertTrue(ppcPage.is_fir_pro_name('请选择'))

        ppcPage.edit_btn_click()
        ppcPage.sleep(4)


if __name__ == '__main__':
    unittest.main()