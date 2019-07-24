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

        provice_option = f'xpath=>//ul[@id="provinceName-ul-li-ul"]/li/a[@itemtext="{provinceName}"]'
        city_option = f'xpath=>//ul[@id="provinceName-ul-li-ul"]/li/a[@itemtext="{cityName}"]'
        district_option = f'xpath=>//ul[@id="provinceName-ul-li-ul"]/li/a[@itemtext="{districtName}"]'
        self.click(self.provinceName_btn)
        self.click(provice_option)
        self.click(self.cityName_btn)
        self.click(self.districtName_btn)
        self.click(district_option)



