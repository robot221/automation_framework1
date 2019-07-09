# -*- coding : utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.res_type import ResType
from pageobjects.zyyhy.res_type_modify import ResTypeModify

class TestAddResTypePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_modify_restype(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_type()

        restype = ResType(driver)
        restype.click_modify_btn()

        modify_restype = ResTypeModify(driver)
        modify_restype.modify_res_type('足球','足球2')

if __name__ == '__main__':
    unittest.main()