# -*- coding : utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.res_type import ResType

class TestResTypePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_search_by_name(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin','admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_type()

        restype = ResType(driver)
        num = restype.query_by_name('羽毛球')
        self.assertEqual(num,'1')

    def test_2_del_res_type(self):
        driver = self.driver
        restype = ResType(driver)
        restype.del_res_type()
        message = restype.get_opt_message()
        self.assertEqual(message,'删除成功！')

if __name__ == '__main__':
    unittest.main()