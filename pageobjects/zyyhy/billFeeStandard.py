# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class BillFeeStandard(BasePage):
    '''物业收费标准'''
    systemName_btn = 'id=>ddl-btn-systemName'

    def select_systemName(self,systemName='中原壹号院'):
        '''选择项目'''
        self.click(self.systemName_btn)
        systemName_option = f'xpath=>//ul[@id="systemName-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
        if self.isElementExist(systemName_option):
            self.click(systemName_option)

    query_btn = 'id=>btn-query-info'
    add_btn = 'id=>btn-add-info'

    modify_btns = 'xpath=>//table[@id="tb-feeBill"]/tbody/tr/td/span/a[@class="calss-modify"]'
    del_btns = 'xpath=>//table[@id="tb-feeBill"]/tbody/tr/td/span/a[@class="calss-delete"]'
    totalCount = 'css=>div#pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    def query_by_systemName(self,systemName='请选择'):
        '''根据项目名称查询'''
        if systemName != '请选择':
            self.select_systemName(systemName)
        self.click(self.query_btn)
        return self.get_totalCount()

    feeTypeName_btn = 'id=>ddl-btn-edit-feeTypeName'
    def select_feeTypeName(self,feeTypeName='物业费'):
        '''选中物业费用类型'''
        self.click(self.feeTypeName_btn)
        feeTypeName_option = f'xpath=>//ul[@id="edit-feeTypeName-ul-li-ul"]/li/a[@itemtext="{feeTypeName}"]'
        feeTypeNames = ('物业费','公共能耗','车位管理费','水费')
        if feeTypeName in feeTypeNames:
            self.click(feeTypeName_option)
    #
    def to_frame(self):
        '''切换到frame'''
        self.driver.switch_to.frame('ueditor_0')
    def to_default_content(self):
        '''从frame中切回主文档'''
        self.driver.switch_to.default_content()

    textarea = 'xpath=>//body[@class="view"]/p[1]'
    save_btn = 'id=>device-edit-button-confirm'

    def add_feeStandard(self,feeTypeName='物业费',content=''):
        self.select_feeTypeName(feeTypeName)
        self.to_frame()
        self.type(self.textarea,content)
        self.to_default_content()
        self.click(self.save_btn)

