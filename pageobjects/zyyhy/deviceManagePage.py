# -*- coding:utf-8 -*-
"""
设备档案
author：daixs
date:2019-07-26
"""
from pywinauto import application

from framework.base_page import BasePage

class DeviceManagePage(BasePage):
    """设备档案"""
    """新增"""
    add_btn = 'id=>btn-add' #新增按钮
    systemName_btn = 'id=>ddl-btn-systemName-edit'  # 选择项目下拉框按钮

    def select_systemName(self, systemName):
        '''新增：选择项目'''
        if systemName != '请选择':
            self.click(self.systemName_btn)
            systemName_option = f'xpath=>//ul[@id="systemName-edit-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
            if self.isElementExist(systemName_option):
                self.click(systemName_option)
    deviceCode = 'id=>edit-deviceCode' #设备编号输入框
    deviceName = 'id=>edit-deviceName' #设备名称输入框

    deviceType_btn = 'id=>ddl-btn-deviceType' # 选择设备类型下拉框按钮
    def select_deviceType(self, deviceType):
        '''新增：选择设备类型'''
        if deviceType != '请选择':
            self.click(self.deviceType_btn)
            deviceType_option = f'xpath=>//ul[@id="deviceType-ul-li-ul"]/li/a[@itemtext="{deviceType}"]'
            if self.isElementExist(deviceType_option):
                self.click(deviceType_option)

    subSystemName_btn = 'id=>ddl-btn-subsystemName-edit' # 选择所属系统下拉框按钮
    def select_subSystemName(self, subSystemName):
        '''新增：选择所属系统'''
        if subSystemName != '请选择':
            self.click(self.subSystemName_btn)
            subSystemName_option = f'xpath=>//ul[@id="subsystemName-edit-ul-li-ul"]/li/a[@itemtext="{subSystemName}"]'
            if self.isElementExist(subSystemName_option):
                self.click(subSystemName_option)

    deviceLocation = 'id=>edit-device-location' #设备位置输入框

    addImgButton = 'id=>addImgButton' #添加图片按钮
    save_btn = 'id=>device-edit-button-confirm' #确定保存按钮
    close_alert_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-header modal-header"]/button[@class="close"]'  # 提示对话框关闭按钮
    def upload(self, filePath):
        """
        上传图片
        :param filePath: 图片路径
        :return:
        """
        self.sleep(1)
        app = application.Application()
        app.connect(title=u'打开', class_name='#32770')
        window = app.window(title=u'打开', class_name='#32770')
        # 文件所在路径不能含有空格
        window["Edit"].type_keys(filePath)
        self.sleep(2)
        window["ScrollBar"].click()
        window[u"打开(O)"].click()
        self.sleep(2)

    def addDevice(self,deviceCode,deviceName,deviceLocation,imgPath=None,systemName='中原壹号院',deviceType='人行抓拍',subSystemName='视频监控'):
        """
        新增设备档案
        :param deviceCode:设备编号
        :param deviceName:设备名称
        :param deviceLocation:设备位置
        :param imgPath:图片路径
        :param systemName:项目名称
        :param deviceType:设备类型
        :param subSystemName:所属系统
        :return:
        """
        self.click(self.add_btn)
        self.select_systemName(systemName)
        self.type(self.deviceCode,deviceCode)
        self.type(self.deviceName,deviceName)
        self.select_deviceType(deviceType)
        self.select_subSystemName(subSystemName)
        self.type(self.deviceLocation,deviceLocation)
        if imgPath:
            self.click(self.addImgButton)
            self.upload(imgPath)
        self.click(self.save_btn)
        self.click(self.close_alert_btn)

    """查询"""
    qSystemName_btn = 'id=>ddl-btn-systemName' # 选择项目下拉框按钮

    def select_qSystemName(self, systemName):
        '''查询：选择项目'''
        if systemName != '请选择':
            self.click(self.qSystemName_btn)
            systemName_option = f'xpath=>//ul[@id="systemName-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
            if self.isElementExist(systemName_option):
                self.click(systemName_option)

    qSubsystemName_btn = 'id=>ddl-btn-subsystemName' # 选择所属系统下拉框按钮
    def select_qSubsystemName(self, subSystemName):
        '''查询：选择所属系统'''
        if subSystemName != '请选择':
            self.click(self.qSubsystemName_btn)
            subSystemName_option = f'xpath=>//ul[@id="subsystemName-ul-li-ul"]/li/a[@itemtext="{subSystemName}"]'
            if self.isElementExist(subSystemName_option):
                self.click(subSystemName_option)

    qDeviceType_btn = 'id=>ddl-btn-query-deviceType' # 选择设备类型下拉框按钮
    def select_qDeviceType(self, deviceType):
        '''查询：选择设备类型'''
        if deviceType != '请选择':
            self.click(self.qDeviceType_btn)
            deviceType_option = f'xpath=>//ul[@id="query-deviceType-ul-li-ul"]/li/a[@itemtext="{deviceType}"]'
            if self.isElementExist(deviceType_option):
                self.click(deviceType_option)

    qDeviceName = 'id=>query-deviceName' #查询：设备名称输入框
    qDeviceCode = 'id=>query-deviceCode' #查询：设备编号输入框

    query_btn = 'id=>btn-query-device' #查询按钮

    def queryDevice(self,qSystemName='请选择',qSubsystemName='请选择',qDeviceType='请选择',qDeviceName=None,qDeviceCode=None):
        """

        :param qSystemName: 选择项目
        :param qSubsystemName: 选择所属系统
        :param qDeviceType: 选择设备类型
        :param qDeviceName: 设备名称
        :param qDeviceCode: 设备编号
        :return:
        """
        self.select_qSystemName(qSystemName)
        self.select_qSubsystemName(qSubsystemName)
        self.select_qDeviceType(qDeviceType)
        if qDeviceName:
            self.type(self.qDeviceName,qDeviceName)
        if qDeviceCode:
            self.type(self.qDeviceCode,qDeviceCode)
        self.sleep(0.5)
        self.click(self.query_btn)

    totalCount = 'css=>div#devices-pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    def xh(self):
        t = True
        self.sleep(1)
        while t:
            self.driver.execute_script('document.getElementById("query-deviceType-ul-li-ul").scrollBy(0,2000)')
            try:
                self.driver.find_element('link_text', '没有更多推荐了，返回首页').click()
                self.sleep(1)
                t = False
            except:
                self.xh()


