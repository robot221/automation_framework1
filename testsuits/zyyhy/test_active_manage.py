# -*- coding: utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.active_m_page import ActivePage
from pageobjects.zyyhy.active_m_page import ActiveDialog

class TestActivePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_query(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin','admin')

        mainpage = MainPage(driver)
        #mainpage.sleep(2)
        mainpage.click_menu_active_m()
        #mainpage.sleep(5)
        activepage = ActivePage(driver)
        activepage.to_frame()
        activepage.query_operate(titlename='测试')
        activepage.sleep(1)
        num = activepage.get_totalCount()
        self.assertEqual(num,'1')

if __name__ == '__main__':
    unittest.main()