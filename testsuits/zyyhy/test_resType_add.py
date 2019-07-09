# -*- coding : utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.res_type import ResType
from pageobjects.zyyhy.res_type_add import ResTypeAdd

class TestAddResTypePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_restype(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_type()

        restype = ResType(driver)
        restype.click_add_btn()

        add_restype = ResTypeAdd(driver)
        add_restype.add_res_type('篮球')

if __name__ == '__main__':
    unittest.main()