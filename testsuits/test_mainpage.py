# -*- coding:utf-8 -*-

import unittest
from pageobjects.hzds.mainpage import MainPage
from pageobjects.hzds.loginpage import LoginPage
from framework.browser_engine import BrowserEngine
class TestMainPage(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        driver = browser.open_browser(self)
        self.driver = driver
    def tearDown(self):
        self.driver.quit()

    def test_main_page(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin','admin')
        mainpage = MainPage(driver)
        self.assertIn("欢迎：",mainpage.get_user_message())
        mainpage.click_xgdfl_menu()
        mainpage.sleep(5)

if __name__ == '__main__':
    unittest.main()