# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import os.path,time
import testsuits
#from testsuits.baidu_homepage_test import BaiduHomepageTest
#from testsuits.baidu_search import BaiduSearch

#suite = unittest.TestSuite(unittest.makeSuite(BaiduHomepageTest))
#suite.addTest(BaiduHomepageTest('test_baidu_homepage'))
#suite.addTest(BaiduSearch('test_baidu_search'))
report_path = os.path.dirname(os.path.abspath('.')) + '/test_reports/'
now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
report_file = report_path + now + 'HTMLTemplate.html'
fp = open(report_file,'wb')

suite = unittest.TestLoader().discover("testsuits",pattern='baidu*.py')

if __name__ == '__main__':
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp,title='项目测试报告',description='用例测试情况')
    runer.run(suite)