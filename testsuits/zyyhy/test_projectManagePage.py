# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.projectManagePage import ProjectManagePage

class TestPMPage(unittest.TestCase):
    """
    项目管理测试用例
    """
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    #@unittest.skip('调试')
    def test_01_addProject(self):
        """新增项目"""
        driver = self.driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')
        mainPage = MainPage(driver)
        mainPage.click_projectManage()

        pmPage = ProjectManagePage(driver)
        projectCode = 'QJY'
        projectName = '曲江印'
        provinceName = '陕西'
        cityName = '西安'
        districtName = '西安'
        addrDetail = '西安市曲江新区南三环以南'
        projectType = '住宅'
        acreage = '10000'
        overview = '曲江印项目以环幕大平层,五星级酒店,甲级写字楼,花园商务城市综合体;12栋环幕大平层,将窗外的繁华街景和优美自然景观揽收眼底,全面吸纳和渗透植物园景观'
        pmPage.addProject(projectCode,projectName,provinceName,cityName,districtName,addrDetail,projectType,acreage,overview)

    #@unittest.skip('调试')
    def test_02_queryProject(self):
        """查询项目"""
        pmPage = ProjectManagePage(self.driver)
        projectCode = 'QJY'
        projectName = '曲江印'
        pmPage.queryProject(projectCode,projectName)
        recordNum = pmPage.get_totalCount()
        self.assertEqual(recordNum,1)

    #@unittest.skip('调试')
    def test_03_modifyProject(self):
        """修改项目"""
        pmPage = ProjectManagePage(self.driver)
        pmPage.queryProject(projectAddr='浙江杭州余杭')
        pmPage.modifyProject(overview='EFC项目,欧美金融城')

    def test_04_delProject(self):
        """删除项目"""
        # driver = self.driver
        # loginpage = LoginPage(driver)
        # loginpage.login('admin', 'admin')
        # mainPage = MainPage(driver)
        # mainPage.click_projectManage()
        pmPage = ProjectManagePage(self.driver)
        pmPage.queryProject(projectName='测试')
        pmPage.delProject()

if __name__ == '__main__':
    unittest.main()


