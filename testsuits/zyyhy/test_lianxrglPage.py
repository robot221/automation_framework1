# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.lianxirenguanliPage import LxrglPage

class TestLianxrglPage(unittest.TestCase):
    """
    联系人管理测试用例
    """

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')
        mainPage = MainPage(driver)
        mainPage.click_lxrgl()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #@unittest.skip('调试')
    def test_01_addContact(self):
        """新增联系人"""
        lxrglPage = LxrglPage(self.driver)
        qphoneName = '赵钱孙'
        qstartTime = '09:00'
        qendTime = '17:00'
        qphoneNumber = '18670892312'
        lxrglPage.add_lianxiren(qphoneName,qstartTime,qendTime,qphoneNumber)

    #@unittest.skip('调试')
    def test_02_queryContact(self):
        '''查询联系人'''
        lxrglPage = LxrglPage(self.driver)
        lxrglPage.query(projectName='中原壹号院',statusName='显示')
        totalNum = lxrglPage.get_totalCount()
        self.assertEqual(totalNum,38)

    #@unittest.skip('调试')
    def test_03_modifyContact(self):
        lxrglPage = LxrglPage(self.driver)
        lxrglPage.modify(qphoneName='代晓松')

   # @unittest.skip('调试')
    def test_04_delContact(self):
        lxrglPage = LxrglPage(self.driver)
        lxrglPage.delete()

    @unittest.skip('方法有问题，先跳过')
    def test_05_switch_state(self):
        lxrglPage = LxrglPage(self.driver)
        lxrglPage.set_switch_view()

if __name__ == '__main__':
    unittest.main()
