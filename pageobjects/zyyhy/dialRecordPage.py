# -*- coding:utf-8 -*-
"""
一键联系-拨打记录
"""
from framework.base_page import BasePage

class DialRecordPage(BasePage):
    projectName_btn = 'id=>ddl-btn-projectName'  # 项目下拉框弹窗按钮--查询

    def select_projectName(self, projectName='请选择'):
        '''选择项目'''
        if projectName != '请选择':
            self.click(self.projectName_btn)
            projectName_option = f'xpath=>//ul[@id="projectName-ul-li-ul"]/li/a[@itemtext="{projectName}"]'
            if self.isElementExist(projectName_option):
                self.click(projectName_option)

    propertyName = 'id=>propertyName' #联系人输入框
    propertyNumber = 'id=>propertyNumber' #联系电话输入框
    qcstartTime = 'id=>qcstartTime' #开始时间输入框
    qcendTime = 'id=>qcendTime' #结束时间输入框
    custName = 'id=>custName' #拨打人输入框
    query_btn = 'id=>btn-query'  # 查询按钮
    totalCount = 'css=>div#pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    def query(self,projectName='请选择',propertyName=None,propertyNumber=None,qcstartTime=None,qcendTime=None,custName=None):
        '''
        查询
        :param projectName: 项目名称
        :param propertyName: 联系人
        :param propertyNumber: 联系电话
        :param qcstartTime: 开始时间
        :param qcendTime: 结束时间
        :param custName: 拨打人
        :return:
        '''
        self.select_projectName(projectName)
        if propertyName != None:
            self.type(self.propertyName,propertyName)
        if propertyNumber != None:
            self.type(self.propertyNumber, propertyNumber)
        if qcstartTime != None:
            self.type(self.qcstartTime, qcstartTime)
        if qcendTime != None:
            self.type(self.qcendTime, qcendTime)
        if custName != None:
            self.type(self.custName, custName)
        self.click(self.query_btn)