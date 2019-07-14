# -*- coding:utf-8 -*-
from framework.base_page import BasePage

class PayReportPage(BasePage):
    '''缴费信息报表'''

    #查询条件
    custNameOrPhone = 'id=>custNameOrPhone' #业主姓名/手机号
    address = 'id=>address' #业主地址
    def select_feeTypeOption(self,feeType):  #选择缴费类型
        feetype_btn = 'id=>ddl-btn-feeTypeName'
        feetype_option = f'xpath=>//ul[@id="feeTypeName-ul-li-ul"]/li/a[@itemtext="{feeType}"]'

        feeTypes = ('物业费','公共能耗','车位管理费','水费')
        if feeType in feeTypes:
            self.click(feetype_btn)
            self.click(feetype_option)

    def select_payTypeOption(self,payType):  #选择支付方式
        paytype_btn = 'id=>ddl-btn-payTypeName'
        paytype_option = f'xpath=>//ul[@id="payTypeName-ul-li-ul"]/li/a[@itemtext="{payType}"]'

        payTypes = ('线下','支付宝','微信')
        if payType in payTypes:
            self.click(paytype_btn)
            self.click(paytype_option)

    nameOrPhone = 'id=>nameOrPhone' #付款联系人姓名/手机号

    def set_startTime(self,time): #设置缴费开始时间
        js = "document.getElementById('startTime').removeAttribute('readonly')"
        startTime = 'id=>startTime'
        self.type(startTime,time)

    def set_endtTime(self,time): #设置缴费结束时间
        js = "document.getElementById('endTime').removeAttribute('readonly')"
        endTime = 'id=>endTime'
        self.type(endTime,time)

    query_btn = 'id=>btn-query-info'

    #查询结果
    detail_links = 'xpath=>//table[@id="tb-feeBill"]/tbody/tr/td/span/a[@title="详情"]' #详情链接

    totalCount = 'css=>div#pg>div.totalCountLabel' # 数据条数

    #查看详情
    owner_phonenumber = 'id=>owner_phonenumber' #业主电话
    close_btn = 'xpath=>//div[@id="edit-bill-modal-content"]/div/button[@class="close close"]' #关闭详情

    def query_and_gettotalnum(self,custNameOrPhone=None,address=None,feeType='全部',payType='全部',nameOrPhone=None,startTime=None,endTime=None):
        if custNameOrPhone != None:
            self.type(self.custNameOrPhone,custNameOrPhone)
        if address != None:
            self.type(self.address,address)
        self.select_feeTypeOption(feeType)
        self.select_payTypeOption(payType)
        if nameOrPhone != None:
            self.type(self.nameOrPhone,nameOrPhone)
        if startTime != None:
            self.set_startTime(startTime)
        if endTime != None:
            self.set_endtTime(endTime)
        self.click(self.query_btn)
        totalCountText = self.find_element(self.totalCount).text
        num = totalCountText.split('共')[1].split('条')[0]
        return num

    def view_detail(self):
        eles = self.find_elements(self.detail_links)
        # print(len(eles))
        eles[0].click()
        owner_phone = self.find_element(self.owner_phonenumber).text
        # self.sleep(3)
        self.click(self.close_btn)
        return owner_phone


    def get_query_results(self):
        L = []
        eles = self.find_elements(self.trs)
        print(len(eles))
        for i in range(len(eles)):
            values = self.trs + f'[{i}]/td[5]'
            print(values)
            v_eles = self.find_elements(values)
            l = []
            for ele in v_eles:

                text = ele.text
                l.append(text)

            L.append(l)
        return L

