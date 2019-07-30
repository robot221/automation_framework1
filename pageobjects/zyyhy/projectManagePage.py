# -*- coding:utf-8 -*-
from framework.base_page import BasePage

class ProjectManagePage(BasePage):
    """项目管理页面"""
    '''新增'''
    add_btn = 'id=>bth-add-project' #新增按钮
    projectCode = 'id=>qserialNo' #项目编码输入框
    projectName = 'id=>qsystemName' #项目名称输入框
    provinceName_btn = 'id=>ddl-btn-provinceName' #选择省按钮
    cityName_btn = 'id=>ddl-btn-cityName' #选择市按钮
    districtName_btn = 'id=>ddl-btn-districtName' #选择区/县按钮
    def select_projectAddress(self,provinceName,cityName,districtName):
        '''
        选择项目地址
        :param provinceName: 省
        :param cityName: 市
        :param districtName:区/县
        :return:
        '''
        provice_option = f'xpath=>//ul[@id="provinceName-ul-li-ul"]/li/a[@itemtext="{provinceName}"]'
        city_option = f'xpath=>//ul[@id="cityName-ul-li-ul"]/li/a[@itemtext="{cityName}"]'
        district_option = f'xpath=>//ul[@id="districtName-ul-li-ul"]/li/a[@itemtext="{districtName}"]'
        self.click(self.provinceName_btn)
        self.click(provice_option)
        self.click(self.cityName_btn)
        self.click(city_option)
        self.click(self.districtName_btn)
        self.click(district_option)

    addrDetail = 'id=>qaddrDetail' #地址详情输入框
    projectType_btn = 'id=>ddl-btn-projectTypeName' #选择项目业态按钮
    def select_projectType(self,projectType='住宅'):
        '''
        选择项目业态
        :param projectType: 项目业态
        :return:
        '''
        projectTypes = ('住宅','商用','办公')
        projectType_option = f'xpath=>//ul[@id="projectTypeName-ul-li-ul"]/li/a[@itemtext="{projectType}"]'
        if projectType in projectTypes:
            self.click(self.projectType_btn)
            self.click(projectType_option)

    acreage = 'id=>acreage' #面积(平方米)输入框
    overview = 'id=>qoverview' #项目简介输入框
    save_btn = 'id=>edit-org-button-confirm' #保存确定按钮
    close_alert_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-header modal-header"]/button[@class="close"]'  # 提示对话框关闭按钮

    def addProject(self,projectCode,projectName,provinceName,cityName,districtName,addrDetail,projectType,acreage,overview):
        """
        新增项目
        :param projectCode: 项目编码
        :param projectName: 项目名称
        :param provinceName: 省
        :param cityName: 市
        :param districtName:区/县
        :param addrDetail: 地址详情
        :param projectType: 项目业态
        :param acreage: 面积(平方米)
        :param overview: 项目简介
        :return:
        """
        self.click(self.add_btn)
        self.type(self.projectCode,projectCode)
        self.type(self.projectName,projectName)
        self.select_projectAddress(provinceName,cityName,districtName)
        self.type(self.addrDetail,addrDetail)
        self.select_projectType(projectType)
        self.type(self.acreage,acreage)
        self.type(self.overview,overview)
        self.click(self.save_btn)
        self.click(self.close_alert_btn)

    """查询"""
    qProjectCode = 'id=>project-code' #查询条件：项目编码输入框
    qProjectName = 'id=>project-name' #查询条件：项目名称输入框
    qProjectAddr = 'id=>project-addr' #查询条件：项目地址输入框
    query_btn = 'id=>btn-query-project' #查询按钮

    def queryProject(self,projectCode=None,projectName=None,projectAddr=None):
        """
        查询项目
        :param projectCode: 项目编码
        :param projectName: 项目名称
        :param projectAddr: 项目地址
        :return:
        """
        if projectCode:
            self.type(self.qProjectCode,projectCode)
        else:
            self.clear(self.qProjectCode)
        if projectName:
            self.type(self.qProjectName,projectName)
        else:
            self.clear(self.qProjectName)
        if projectAddr:
            self.type(self.qProjectAddr,projectAddr)
        else:
            self.clear(self.qProjectAddr)
        self.click(self.query_btn)

    totalCount = 'css=>div#pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    """修改"""
    modify_btns = 'xpath=>//a[@class="calss-modify" and @title="修改"]'  # 修改按钮
    def modifyProject(self,projectCode=None,projectName=None,provinceName=None,cityName=None,districtName=None,addrDetail=None,projectType=None,acreage=None,overview=None):
        """
        修改项目
        :param projectCode: 项目编码
        :param projectName: 项目名称
        :param provinceName: 省
        :param cityName: 市
        :param districtName:区/县
        :param addrDetail: 地址详情
        :param projectType: 项目业态
        :param acreage: 面积(平方米)
        :param overview: 项目简介
        :return:
        """
        if self.get_totalCount() > 0:
            modifyBtns = self.find_elements(self.modify_btns)
            modifyBtns[0].click()
            if projectCode:
                self.type(self.projectCode, projectCode)
            if projectName:
                self.type(self.projectName, projectName)
            if provinceName and cityName and districtName:
                self.select_projectAddress(provinceName, cityName, districtName)
            if addrDetail:
                self.type(self.addrDetail, addrDetail)
            if projectType:
                self.select_projectType(projectType)
            if acreage:
                self.type(self.acreage, acreage)
            if overview:
                self.type(self.overview, overview)
            self.click(self.save_btn)
            self.click(self.close_alert_btn)

    '''删除'''
    del_btns = 'xpath=>//a[@class="calss-del" and @title="删除"]'  # 删除按钮
    confirm_del_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a[1]'  # 确定删除按钮
    def delProject(self):
        '''
        删除
        :return:
        '''
        if self.get_totalCount() > 0:
            delBtns = self.find_elements(self.del_btns)
            delBtns[-1].click()
            self.click(self.confirm_del_btn)
            self.click(self.close_alert_btn)


    """跳转到轮播图"""
    banner_btns = 'xpath=>//a[@class="query-banner" and @title="轮播图"]'  #轮播图按钮

    def to_bannerPage(self):
        if self.get_totalCount() > 0:
            bannerBtns = self.find_elements(self.banner_btns)
            bannerBtns[0].click()




