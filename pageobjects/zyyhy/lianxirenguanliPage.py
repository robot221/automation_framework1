# -*- coding:utf-8 -*-
"""
联系人管理功能
新增
查询
修改
修改显示状态
删除
author：daixs
date:2019-07-22
"""
from framework.base_page import BasePage
from random import randint
class LxrglPage(BasePage):
    """
    新增
    """
    add_btn = 'id=>btn-add' #新增按钮
    select_systemName_btn = 'id=>ddl-btn-conEditSystemName' #项目下拉框弹窗按钮
    def select_systemName(self,systemName='中原壹号院'):
        '''选择项目'''
        self.click(self.select_systemName_btn)
        systemName_option = f'xpath=>//ul[@id="conEditSystemName-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
        if self.isElementExist(systemName_option):
            self.click(systemName_option)

    address_list = 'xpath=>//div[@id="address-group-list"]/span/label/div/span'
    def check_address(self,check_num=2):
        """选择楼幢"""
        eles = self.find_elements(self.address_list)
        if len(eles) > check_num:
            for index in range(check_num):
                if eles[index].get_attribute("class") != 'checked':
                    eles[index].click()
        else:
            for ele in eles:
                if ele.getAttribute("class") != 'checked':
                    ele.click()

    qphoneName = 'id=>qphoneName' #联系人名称输入框
    qstartTime = 'id=>qstartTime' #可拨打时间段：开始时间输入框
    qendTime = 'id=>qendTime' #可拨打时间段：结束时间输入框
    qphoneNumber = 'id=>qphoneNumber' #联系人电话输入框
    save_btn = 'id=>edit-contact-button-confirm' #确定保存按钮

    def add_lianxiren(self,qphoneName,qstartTime,qendTime,qphoneNumber,systemName='中原壹号院',check_num=2):
        """
        新增联系人
         联系人名称，可拨打时间段：开始时间，可拨打时间段：结束时间，联系人电话，项目名称，选择楼栋数
        """
        self.click(self.add_btn)
        self.select_systemName(systemName)
        self.check_address(check_num)
        self.type(self.qphoneName,qphoneName)
        self.type(self.qstartTime,qstartTime)
        self.type(self.qendTime,qendTime)
        self.type(self.qphoneNumber,qphoneNumber)
        self.click(self.save_btn)

    """
    查询
    """
    projectName_btn = 'id=>ddl-btn-projectName' #项目下拉框弹窗按钮--查询
    def select_projectName(self,projectName='请选择'):
        '''选择项目'''
        if projectName != '请选择':
            self.click(self.projectName_btn)
            projectName_option = f'xpath=>//ul[@id="projectName-ul-li-ul"]/li/a[@itemtext="{projectName}"]'
            if self.isElementExist(projectName_option):
                self.click(projectName_option)

    statusName_btn = 'id=>ddl-btn-statusName' #状态下拉框弹窗按钮--查询
    def select_statusName(self,statusName='显示状态'):
        '''选择状态'''
        if statusName != '显示状态':
            self.click(self.statusName_btn)
            statusName_option = f'xpath=>//ul[@id="statusName-ul-li-ul"]/li/a[@itemtext="{statusName}"]'
            if self.isElementExist(statusName_option):
                self.click(statusName_option)

    query_btn = 'id=>btn-query' #查询按钮

    totalCount = 'css=>div#pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    def query(self,projectName='请选择',statusName='显示状态'):
        '''查询'''
        self.select_projectName(projectName)
        self.select_statusName(statusName)
        self.click(self.query_btn)
    """
    修改 删除
    """
    modify_btns = 'xpath=>//a[@class="calss-modify" and @title="修改"]'
    del_btns = 'xpath=>//a[@class="class-delete" and @title="删除"]'
    def modify(self,qphoneName=None,qstartTime=None,qendTime=None,qphoneNumber=None,check_num=3):
        '''
        修改
        联系人名称，可拨打时间段：开始时间，可拨打时间段：结束时间，联系人电话，选择楼栋数
        '''
        if self.get_totalCount() > 0:
            modify_eles = self.find_elements(self.modify_btns)
            index = randint(0,len(modify_eles)-1)
            modify_eles[index].click()
            if check_num > 0:
                self.check_address(check_num)
            if qphoneName != None:
                self.type(self.qphoneName, qphoneName)
            if qstartTime != None:
                self.type(self.qstartTime, qstartTime)
            if qendTime != None:
                self.type(self.qendTime, qendTime)
            if qphoneNumber != None:
                self.type(self.qphoneNumber, qphoneNumber)
            self.click(self.save_btn)

    del_confirm_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a[1]' #确认删除按钮
    def delete(self):
        if self.get_totalCount() > 0:
            del_eles = self.find_elements(self.del_btns)
            index = randint(0,len(del_eles)-1)
            del_eles[index].click()
            self.click(self.del_confirm_btn)
    '''显示状态变更'''

    switchBtns = 'name=>switchBtn'
    operate_close_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-header modal-header"]/button'
    def set_switch_view(self,switch_on=False):
        '''
        显示状态变更
        :param switch_on: False 关闭显示状态，True开启显示状态
        :return:
        '''
        if self.get_totalCount() > 0:
            switchs = self.find_elements(self.switchBtns)

            if switch_on:

                for switch in switchs:
                    if self.get_attr_value(switch,"isopen") == "false":
                        switch.click()
                        self.click(self.operate_close_btn)
                        self.sleep(1)
                        switchs = self.find_elements(self.switchBtns)
            else:
                for switch in switchs:
                    if self.get_attr_value(switch,"isopen") == "true":
                        switch.click()
                        self.click(self.operate_close_btn)
                        self.sleep(1)
                        switchs = self.find_elements(self.switchBtns)


