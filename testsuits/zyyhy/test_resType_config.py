# -*- coding : utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.res_type import ResType
from pageobjects.zyyhy.res_type_config import ResTypeConfig

class TestAddResTypePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #@unittest.skip("调试，暂不执行")
    def test_add_config_restype(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_type()

        restype = ResType(driver)
        restype.click_plus_btn()
        restype.sleep(1)
        config_restype = ResTypeConfig(driver)
        config_restype.add_config('Wifi','无线网络')
        message = config_restype.get_opt_message()

        self.assertEqual(message, '操作成功！')
        config_restype.sleep(3)

    def test_modify_config_restype(self):
        driver = self.driver
        # loginpage = LoginPage(driver)
        # loginpage.login('admin', 'admin')
        #
        # mainpage = MainPage(driver)
        # mainpage.click_menu_res_type()

        restype = ResType(driver)
        restype.click_plus_btn()
        restype.sleep(1)
        config_restype = ResTypeConfig(driver)
        config_restype.modify_config('Wifi3','无线网络3')
        #config_restype.sleep(1)
        message = config_restype.get_opt_message()

        self.assertEqual(message,'操作成功！')

if __name__ == '__main__':
    unittest.main()