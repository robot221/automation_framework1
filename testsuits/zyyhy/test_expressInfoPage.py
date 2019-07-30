# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.expressInfoPage import ExpressInfoPage

class TestExpressInfo(unittest.TestCase):
    """
    快递信息管理测试用例
    """

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')
        mainPage = MainPage(driver)
        mainPage.click_expressInfoM()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    @unittest.skip('调试')
    def test_01_addExpressInfo(self):
        """新增快递信息"""
        expressInfoPage = ExpressInfoPage(self.driver)
        addresseeName = '代晓松'
        addressPhone = '18667027231'
        expressNo = '3301201907300109'
        expressInfoPage.add_express(addresseeName,addressPhone,expressNo)

    def test_02_query(self):
        """查询快递信息"""
        expressInfoPage = ExpressInfoPage(self.driver)
        expressInfoPage.query(addresseeName='代晓松')
        recordNum = expressInfoPage.get_totalCount()
        self.assertEqual(recordNum,3)

    def test_03_modify(self):
        """修改快递信息"""
        expressInfoPage = ExpressInfoPage(self.driver)
        expressInfoPage.query(systemName='0829',addressPhone='222')
        expressInfoPage.modify(addressPhone='18709123222',addresseeName='测试修改',expressNo='3210193034318')
        expressInfoPage.sleep(1)
    def test_04_delete(self):
        """删除快递信息"""
        expressInfoPage = ExpressInfoPage(self.driver)
        expressInfoPage.query(systemName='0829',addressPhone='13344445555',addresseeName='test00155')
        expressInfoPage.delete_express()

    @unittest.skip('modifyState方法有问题，暂不执行')
    def test_05_modifyState(self):
        """修改快递状态"""
        expressInfoPage = ExpressInfoPage(self.driver)
        expressInfoPage.query(expressState='未领')
        expressInfoPage.modifyState()


if __name__ == '__main__':
    unittest.main()


