# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomepage

class BaiduHomepageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_homepage(self):
        baidu_home_page = BaiduHomepage(self.driver)
        baidu_home_page.type_search('selenium')
        baidu_home_page.submit_button()
        baidu_home_page.sleep(1)
        baidu_home_page.get_windows_img()
        self.assertIn('selenium',baidu_home_page.get_page_title())

    def test_seach2(self):
        baidu_home_page = BaiduHomepage(self.driver)
        baidu_home_page.type_search('python')
        baidu_home_page.submit_button()
        baidu_home_page.sleep(1)
        baidu_home_page.get_windows_img()
        self.assertIn('python', baidu_home_page.get_page_title())
if __name__ == '__main__':
    unittest.main()