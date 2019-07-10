# -*- coding: utf-8 -*-

from framework.base_page import BasePage
from pywinauto import application  #Spy++
class BillBIPage(BasePage):
    #项目名称选择按钮
    select_btn = 'id=>ddl-btn-systemName'
    #中原壹号院选项
    zyyhy_option = 'xpath=>//ul[@id="systemName-ul-li-ul"]/li[2]'
    #批次号
    qBatchCode = 'id=>qBatchCode'

    #开始时间
    qCreateDate = 'id=>qCreateDate'
    #结束时间
    qEndDate = 'id=>qEndDate'
    #查询按钮
    query_btn = 'id=>btn-query-card'
    #批量导入按钮
    upload_btn = 'id=>btn-upload'
    #模板下载按钮
    download_btn = 'id=>btn-download'

    #查看明细链接
    dealInfos = 'xpath=>//a[@class="deal-info" and @title="明细信息"]'

    #批量导入明细
    #所属小区：
    projectName = 'id=>projectName'
    #状态选择按钮
    select_status_btn = 'id=>ddl-btn-statusName'

    #选择状态
    def select_status(self,status='请选择'):
        self.click(self.select_status_btn)
        #self.sleep(3)
        if status == '成功':
            self.click('xpath=>//ul[@id="statusName-ul-li-ul"]/li/a[@itemtext="成功"]')
        elif status == '失败':
            self.click('xpath=>//ul[@id="statusName-ul-li-ul"]/li/a[@itemtext="失败"]')
        else:
            self.click('xpath=>//ul[@id="statusName-ul-li-ul"]/li/a[@itemtext="请选择"]')

    #查询明细按钮
    detail_query_btn = 'id=>btn-queryDetail-card'
    #记录总数
    detail_record_num = 'css=>div#pg-detail>div.totalCountLabel'
    #确定按钮
    confirm_btn = 'xpath=>//div[@id="show-detail-modal-content"]/div[@class="modal-footer modal-footer"]/a'
    #关闭按钮
    close_btn = 'xpath=>//div[@id="show-detail-modal-content"]/div[@class="modal-header modal-header"]/button'
    #导入后操作提示确定按钮
    operate_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a'
    #批量导入
    def upload(self,filePath):
        self.click(self.upload_btn)
        self.sleep(2)
        app = application.Application()
        app.connect(title=u'打开', class_name='#32770')
        window = app.window(title=u'打开', class_name='#32770')
        # 文件所在路径不能含有空格
        window["Edit"].type_keys(filePath)
        self.sleep(2)
        window["ScrollBar"].click()
        window[u"打开(O)"].click()
        self.sleep(2)

    #批量导入操作
    def batchImportBill(self,filePath):
        self.click(self.select_btn)
        self.click(self.zyyhy_option)
        self.upload(filePath)
        self.click(self.operate_btn)

    #查看导入明细并返回失败数目
    def view_detail_and_get_failNum(self):
        eles = self.find_elements(self.dealInfos)
        eles[0].click()
        #self.click(self.select_status_btn)
        self.select_status(status='失败')
        self.click(self.detail_query_btn)
        totalCountEle = self.find_element(self.detail_record_num)
        failNum = totalCountEle.text.split('共')[1].split('条')[0]
        self.click(self.close_btn)
        return failNum


