# -*- coding:utf-8 -*-
from framework.base_page import BasePage

class ExpressInfoPage(BasePage):
    '''
    快递信息管理页面
    '''
    """
    新增
    """
    add_btn = 'id=>btn-add-express' #新增按钮
    systemName_btn = 'id=>ddl-btn-systemIdEdit' #选择项目下拉框按钮
    def select_systemName(self, systemName='请选择'):
        '''新增：选择项目'''
        if systemName != '请选择':
            self.click(self.systemName_btn)
            systemName_option = f'xpath=>//ul[@id="systemIdEdit-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
            if self.isElementExist(systemName_option):
                self.click(systemName_option)

    expressName_btn = 'id=>ddl-btn-expressNameId' #选择快递公司下拉框按钮
    def select_expressName(self, expressName='请选择'):
        '''新增：选择快递公司'''
        expressNames = ('圆通','中通','汇通','韵达','百世汇通','顺丰','全峰')
        expressName_option = f'xpath=>//ul[@id="expressNameId-ul-li-ul"]/li/a[@itemtext="{expressName}"]'
        if expressName in expressNames:
            self.click(self.expressName_btn)
            self.click(expressName_option)

    addresseeName= 'id=>addresseeName' #收件人姓名输入框
    addressPhone = 'id=>addressPhone' #收件人电话输入框
    expressNo = 'id=>expressNo' #快递单号输入框
    save_btn = 'id=>edit-express-button-confirm' #新增确定按钮

    def add_express(self,addresseeName,addressPhone,expressNo,systemName='中原壹号院',expressName='圆通'):
        '''

        :param addresseeName: 收件人姓名
        :param addressPhone: 收件人电话
        :param expressNo: 快递单号
        :param systemName: 选择项目
        :param expressName: 选择快递公司
        :return:
        '''
        self.click(self.add_btn)
        self.select_systemName(systemName)
        self.select_expressName(expressName)
        self.type(self.addresseeName,addresseeName)
        self.type(self.addressPhone,addressPhone)
        self.type(self.expressNo,expressNo)
        self.click(self.save_btn)

    """
    查询
    """
    qsystemName_btn = 'id=>ddl-btn-qSystemId' #选择项目下拉框按钮
    def select_qsystemName(self, systemName='请选择'):
        '''查询：选择项目'''
        self.click(self.qsystemName_btn)
        systemName_option = f'xpath=>//ul[@id="qSystemId-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
        if self.isElementExist(systemName_option):
            self.click(systemName_option)

    qAddresseePhone = 'id=>qAddresseePhone' #收件人电话输入框
    qAddresseeName = 'id=>qAddresseeName' #收件人姓名输入框
    qExpressNo = 'id=>qExpressNo' #快递单号输入框
    qexpressName_btn = 'id=>ddl-btn-qexpressName' #选择快递公司下拉框按钮
    def select_qexpressName(self, expressName='请选择'):
        '''查询：选择快递公司'''
        expressNames = ('请选择','圆通','中通','汇通','韵达','百世汇通','顺丰','全峰')
        expressName_option = f'xpath=>//ul[@id="qexpressName-ul-li-ul"]/li/a[@itemtext="{expressName}"]'
        if expressName in expressNames:
            self.click(self.qexpressName_btn)
            self.click(expressName_option)

    expressState_btn = 'id=>ddl-btn-qexpressStateName' #选择快递状态下拉框按钮
    def select_qexpressState(self, expressState='请选择'):
        '''查询：选择快递状态'''
        expressStates = ('请选择','未领','已领')
        expressState_option = f'xpath=>//ul[@id="qexpressStateName-ul-li-ul"]/li/a[@itemtext="{expressState}"]'
        if expressState in expressStates:
            self.click(self.expressState_btn)
            self.click(expressState_option)
    query_btn = 'id=>btn-query-express'

    def query(self,systemName='请选择',addressPhone=None,addresseeName=None,expressNo=None,expressName='请选择',expressState='请选择'):
        '''
        查询
        :param systemName: 项目名称
        :param addressPhone:收件人电话
        :param addresseeName:收件人姓名
        :param expressNo:快递单号
        :param expressName:快递公司
        :param expressState:状态
        :return:
        '''
        self.select_qsystemName(systemName)
        if addressPhone != None:
            self.type(self.qAddresseePhone,addressPhone)
        else:
            self.clear(self.qAddresseePhone)
        if addresseeName != None:
            self.type(self.qAddresseeName,addresseeName)
        else:
            self.clear(self.qAddresseeName)
        if expressNo != None:
            self.type(self.qExpressNo,expressNo)
        else:
            self.clear(self.qExpressNo)
        self.select_qexpressName(expressName)
        self.select_qexpressState(expressState)
        self.click(self.query_btn)


    totalCount = 'css=>div#pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    """
    修改状态
    """
    modifyState_btns = 'xpath=>//a[@class="deal-info" and @title="状态修改"]' # 修改状态按钮
    state_cols = 'xpath=>//table[@id="tb-Express"]/tbody/tr/td[9]' #状态列
    confirm_modify_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a[1]'
    close_operate_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-header modal-header"]/button[@class="close"]'

    def modifyState(self,state='已领'):
        '''

        :param state:
        :return:
        '''
        if self.get_totalCount() > 0:
            stateBtns = self.find_elements(self.modifyState_btns) #全部操作按钮
            stateCols = self.find_elements(self.state_cols) #状态列所有元素
            states = ['已领','未领']
            if state in states:
                for index,stateCol in enumerate(stateCols):
                    if stateCol.text != state:
                        stateBtns[index].click()
                        self.click(self.confirm_modify_btn)
                        self.sleep(1)
                        self.click(self.close_operate_btn)

    """
    修改
    """
    modify_btns = 'xpath=>//a[@class="calss-modify" and @title="修改"]' # 修改按钮
    mexpressState_btn = 'id=>ddl-btn-expressStateId1' #状态下拉框按钮
    def select_mexpressState(self, expressState='请选择'):
        '''修改：选择快递状态'''
        expressStates = ('未领','已领')
        expressState_option = f'xpath=>//ul[@id="expressStateId1-ul-li-ul"]/li/a[@itemtext="{expressState}"]'
        if expressState in expressStates:
            self.click(self.mexpressState_btn)
            self.click(expressState_option)
    def modify(self,systemName='请选择',addressPhone=None,addresseeName=None,expressNo=None,expressName='请选择',expressState='请选择'):
        '''
        修改
        :param systemName:
        :param addressPhone:
        :param addresseeName:
        :param expressNo:
        :param expressName:
        :param expressState:
        :return:
        '''
        if self.get_totalCount() > 0:
            modifyBtns = self.find_elements(self.modify_btns)
            modifyBtns[0].click()

            self.select_systemName(systemName)
            if addressPhone != None:
                self.type(self.addressPhone,addressPhone)
            if addresseeName != None:
                self.type(self.addresseeName,addresseeName)
            if expressNo != None:
                self.type(self.expressNo,expressNo)
            self.select_expressName(expressName)
            self.select_mexpressState(expressState)
            self.click(self.save_btn)

    '''
    删除
    '''
    del_btns = 'xpath=>//a[@class="class-delete" and @title="删除"]'  # 删除按钮
    confirm_del_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a[1]' #确定删除按钮

    def delete_express(self):
        '''
        删除
        :return:
        '''
        if self.get_totalCount() > 0:
            delBtns = self.find_elements(self.del_btns)
            delBtns[-1].click()
            self.click(self.confirm_del_btn)
            self.click(self.close_operate_btn)
