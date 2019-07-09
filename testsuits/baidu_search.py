# coding:utf-8

import time,unittest
from framework.browser_engine import BrowserEngine

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()
    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium1' in self.driver.title
            print('test pass')
        except Exception as e:
            print('Test fail:',format(e))

if __name__ == '__main__':
    unittest.main()