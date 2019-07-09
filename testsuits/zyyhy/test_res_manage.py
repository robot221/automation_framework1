# -*- coding : utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.res_manage_page import ResManagePage
from pageobjects.zyyhy.res_manage_add import ResMngAddPage
from pageobjects.zyyhy.res_manage_modify import ModifyResource
from pageobjects.zyyhy.res_manage_view import ViewResource
from pageobjects.zyyhy.res_manage_record import ResourceBookRecord
class TestResManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @unittest.skip("单例调试，暂不执行")
    def test_add_resource(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_manage()
        mainpage.sleep(2)
        resManage = ResManagePage(driver)
        resManage.click_add_dialog()

        resMngAddpage = ResMngAddPage(driver)

        resName = '羽毛球'
        typeName = '羽毛球'
        address = '羽毛球'
        phone = '18667027231'
        passnum = 3
        imgUrl = r'C:\Users\Hi\Desktop\1555319477282.jpg'
        resDesc = '来一次酣畅淋漓的比赛'
        validDate = '2019-07-03'
        expireDate = '2021-07-31'
        startTime,endTime = '07:00','18:00'

        resMngAddpage.add_resource(resName, typeName, address, phone, passnum, imgUrl, resDesc, validDate, expireDate,
                     startTime, endTime)


    #修改公共资源
    @unittest.skip("单例调试，暂不执行")
    def test_modify_resource(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_manage()
        mainpage.sleep(2)
        resManage = ResManagePage(driver)
        resManage.click_modify_dialog()

        modifyRes = ModifyResource(driver)

        resName = '羽毛球1'
        #typeName = '羽毛球'
        address = '羽毛球1'
        phone = '18667027233'
        #passnum = 3
        imgUrl = r'C:\Users\Hi\Desktop\fGqWeLbnkDlvCFF.jpg'
        resDesc = '来打羽毛球！'
        validDate = '2019-07-04'
        expireDate = '2031-07-31'
        #startTime, endTime = '07:00', '18:00'
        modifyRes.modify_resource(resName,address,phone,imgUrl,resDesc,validDate,expireDate)
        modifyRes.sleep(3)

    @unittest.skip("单例调试，暂不执行")
    def test_res_view(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_manage()
        mainpage.sleep(2)
        resManage = ResManagePage(driver)
        resManage.click_view_dialog()

        viewRes = ViewResource(driver)

        info = viewRes.get_viewInfo()

        str = ','.join(info)
        self.assertEqual(str,'羽毛球1,羽毛球')

    def test_res_record(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')

        mainpage = MainPage(driver)
        mainpage.click_menu_res_manage()
        mainpage.sleep(2)
        resManage = ResManagePage(driver)
        resManage.click_record_dialog()

        recordpage = ResourceBookRecord(driver)
        num = recordpage.query_by_orderNo('343345')
        self.assertEqual(num,'0')


if __name__ == '__main__':
    unittest.main()

