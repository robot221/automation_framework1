# -*- coding:utf-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.zyyhy.loginpage import LoginPage
from pageobjects.zyyhy.mainpage import MainPage
from pageobjects.zyyhy.parkingNoticePage import ParkingNoticePage

class TestExpressInfo(unittest.TestCase):
    """
    园区公告管理测试用例
    """

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        driver = browser.open_browser(cls)
        cls.driver = driver
        loginpage = LoginPage(driver)
        loginpage.login('admin', 'admin')
        mainPage = MainPage(driver)
        mainPage.click_parkingNoticeM()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_addNotice(self):
        """新增公告"""
        noticePage = ParkingNoticePage(self.driver)
        systemName = '测试项目'
        noticeTypeName = '通知'
        noticeTitle = '元旦放假通知'
        content = """
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺。。。
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        2019年通知，元旦放假时间时间18年30号到19年1月1号，2号开始上班，希望大家下班关闭窗户，灯和空调，另外祝大家新年快乐，2019年旺旺
        """
        noticePage.addNotice(systemName=systemName,noticeTypeName=noticeTypeName,noticeTitle=noticeTitle,content=content)

    def test_02_queryNotice(self):
        """查询公告"""
        noticePage = ParkingNoticePage(self.driver)
        noticePage.queryNotice(qName='元旦放假通知')
        recordNum = noticePage.get_totalCount()
        self.assertEqual(recordNum,2)

    def test_03_modifyNotice(self):
        """修改公告"""
        noticePage = ParkingNoticePage(self.driver)
        noticePage.queryNotice(qName='测试小屋',noticeTypeName='活动')
        noticeTypeName = '新闻'
        noticeTitle = '淘宝京东分庭抗礼，亚马逊“我溜了”'
        content = '近日，亚马逊中国正式停售纸质图书，在官网将图书分类移除，所有图书类读物统一变为Kindle商店和Kindle电子书的分类，从此亚马逊网站退出纸质图书的售卖。'
        noticePage.modifyNotice(noticeTypeName=noticeTypeName,noticeTitle=noticeTitle,content=content)

    def test_04_deleteNotice(self):
        """删除公告"""
        noticePage = ParkingNoticePage(self.driver)
        noticePage.queryNotice(systemName='0829')
        noticePage.delNotice()

if __name__ == '__main__':
    unittest.main()