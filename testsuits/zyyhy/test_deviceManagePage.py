# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.deviceManagePage import DeviceManagePage

class TestDMPage(unittest.TestCase):
    """
    设备档案测试用例
    """
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_addDevice(self):
        '''新增设备'''
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin','admin')
        mainPage = MainPage(driver)
        mainPage.click_deviceManage()

        dmPage = DeviceManagePage(driver)
        dmPage.addDevice(deviceCode='renxing7294',deviceName='3幢1单元人行相机1',deviceLocation='3幢1单元',imgPath=r'D:\data\t1\timg.jpg')

    def test_2_queryDevice(self):
        '''查询设备'''
        driver = self.driver
        dmPage = DeviceManagePage(driver)
        dmPage.queryDevice(qDeviceName='1单元')
        recordNum = dmPage.get_totalCount()
        self.assertEqual(recordNum,3)


if __name__ == '__main__':
    unittest.main()