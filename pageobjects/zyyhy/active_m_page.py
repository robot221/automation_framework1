# -*- coding: utf-8 -*-

from framework.base_page import BasePage

class ActivePage(BasePage):
    frame = 'id=>content-iframe'

    ownerName = 'id=>ownerName' #查询条件：业主昵称输入框
    titleName = 'id=>titleName' #查询条件：标题输入框
    startTime = 'id=>startTime' #查询条件：开始时间输入框
    endTime = 'id=>endTime' #查询条件：结束时间输入框

    #切换到frame
    def to_frame(self):
        self.driver.switch_to.frame('content-iframe')
    #选择活动状态
    def select_state_option(self,state='全部'):
        select_btn = 'id=>ddl-btn-activeStatusName'
        self.click(select_btn)
        if state == '报名中':
            self.click('xpath=>//ul[@id="activeStatusName-ul-li-ul"]/li/a[@itemtext="报名中"]')
        elif state == '报名结束':
            self.click('xpath=>//ul[@id="activeStatusName-ul-li-ul"]/li/a[@itemtext="报名结束"]')
        elif state == '活动中':
            self.click('xpath=>//ul[@id="activeStatusName-ul-li-ul"]/li/a[@itemtext="活动中"]')
        elif state == '活动结束':
            self.click('xpath=>//ul[@id="activeStatusName-ul-li-ul"]/li/a[@itemtext="活动结束"]')
        else:
            self.click('xpath=>//ul[@id="activeStatusName-ul-li-ul"]/li/a[@itemtext="全部"]')

    query_btn = 'id=>btn-query' #查询按钮

    #查询结果数量
    def get_totalCount(self):
        totalCount = 'css=>div.totalCountLabel'
        ele = self.find_element(totalCount)
        txt_content = ele.text
        num = txt_content.split('共')[1].split('条')[0]
        return num

    #查询操作
    def query_operate(self,ownername=None,titlename=None,starttime=None,endtime=None,state='全部'):
        if ownername != None:
            self.type(self.ownerName,ownername)
        if titlename != None:
            self.type(self.titleName,titlename)
        if starttime != None:
            self.type(self.startTime,starttime)
        if endtime != None:
            self.type(self.endTime,endtime)
        self.select_state_option(state)
        self.click(self.query_btn)


    pass_btns = 'xpath=>//table[@id="tb_actives"]/tbody/tr/td/span/a[@title="通过"]' #审核通过按钮
    refuse_btns = 'xpath=>//table[@id="tb_actives"]/tbody/tr/td/span/a[@title="拒绝"]' #审核拒绝按钮
    detail_btns = 'xpath=>//table[@id="tb_actives"]/tbody/tr/td/span/a[@title="活动详情"]' #活动详情按钮
    delete_btns = 'xpath=>//table[@id="tb_actives"]/tbody/tr/td/span/a[@title="删除"]' #删除按钮

    #点击审核通过按钮
    def click_pass_btn(self):
        eles = self.find_elements(self.pass_btns)
        eles[0].click()

    # 点击审核拒绝按钮
    def click_refuse_btn(self):
        eles = self.find_elements(self.refuse_btns)
        eles[0].click()

    # 点击活动详情按钮
    def click_detail_btn(self):
        eles = self.find_elements(self.detail_btns)
        eles[0].click()


    # 点击删除按钮
    def click_delete_btn(self):
        eles = self.find_elements(self.delete_btns)
        eles[0].click()

class ActiveDialog(BasePage):
    operateMessage = 'id=>operateMessage' #操作描述信息
    close_btn = 'xpath=>//div[@id="operate-div-modal-content"]/div[@class="modal-header modal-header"]/button' #关闭对话框
    confirm_btn = 'id=>operate-div-button-confirm'
    operate_cf_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a'

    def pass_refuse_del(self,message):
        self.type(self.operateMessage,message)
        self.click(self.confirm_btn)
        self.click(self.operate_cf_btn)