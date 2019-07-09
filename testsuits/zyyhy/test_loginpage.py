# -*- coding: utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage

class TestLoge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        username = 'admin'
        password = 'admin'

        driver = self.driver

        loginPage = LoginPage(driver)
        loginPage.login(username,password)

        mainPage = MainPage(driver)
        loginInfo = mainPage.login_verify()

        self.assertEqual(loginInfo,username)

if __name__ == '__main__':
    unittest.main()

