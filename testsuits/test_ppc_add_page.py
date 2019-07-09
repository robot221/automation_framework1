# -*- coding:utf-8 -*-

import unittest
from pageobjects.hzds.mainpage import MainPage
from pageobjects.hzds.loginpage import LoginPage
from framework.browser_engine import BrowserEngine
from pageobjects.hzds.ppc_page import PPCPage
from pageobjects.hzds.ppc_add_page import PpcAddPage

class TestPPCPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_add_first_catagory(self):
        """新增一级分类"""
        driver = self.driver
        loginPage = LoginPage(driver)
        mainPage = MainPage(driver)
        ppcPage = PPCPage(driver)
        p_add_page = PpcAddPage(driver)

        loginPage.login('admin', 'admin')
        mainPage.click_xgdfl_menu()
        mainPage.sleep(1)

        #self.assertTrue(ppcPage.is_fir_pro_name('请选择'))

        ppcPage.add_btn_click()
        ppcPage.sleep(1)
        project_num = p_add_page.get_eprojectName_num()
        self.assertEqual(3,project_num)
        p_add_page.select_pro_name()
        p_add_page.sleep(3)
        p_add_page.type_name("消防设施4","消防设施4")
        p_add_page.submit_click()
        p_add_page.sleep(3)
        self.assertEqual('保存成功！',p_add_page.get_succ_text())
        p_add_page.click_div_btn()
        p_add_page.sleep(3)

    def test_2_add_second_catagory(self):
        """新增二级分类"""
        driver = self.driver
        #loginPage = LoginPage(driver)
        #mainPage = MainPage(driver)
        ppcPage = PPCPage(driver)
        p_add_page = PpcAddPage(driver)

        #loginPage.login('admin', 'admin')
        #mainPage.click_xgdfl_menu()
        #mainPage.sleep(1)

        #self.assertTrue(ppcPage.is_fir_pro_name('请选择'))

        ppcPage.add_btn_click()
        ppcPage.sleep(1)
        #project_num = p_add_page.get_eprojectName_num()
        #self.assertEqual(3,project_num)
        p_add_page.select_pro_name()
        p_add_page.sleep(1)
        p_add_page.select_s_elevelName()
        p_add_page.sleep(1)
        p_add_page.select_eparentName()
        p_add_page.type_name("消防设施分类5","消防设施分类5")
        p_add_page.submit_click()
        p_add_page.sleep(3)
        self.assertEqual('保存成功！',p_add_page.get_succ_text())
        p_add_page.click_div_btn()
        p_add_page.sleep(3)


if __name__ == '__main__':
    unittest.main()