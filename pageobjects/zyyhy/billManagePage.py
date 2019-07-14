# -*- coding:utf-8 -*-

from framework.base_page import BasePage
class BillMPage(BasePage):
    #账单月份，移除readonly属性，使其可以输入
    js = "document.getElementById('billMonth').removeAttribute('readonly')"
    billMonth = 'id=>billMonth'
    #缴费人/地址
    nameOrRoom = 'id=>nameOrRoom'
    query_btn = 'id=>btn-query-info'

    def query_by_month_address(self,month,address):
        '''根据账单月份，缴费人/地址查询'''
        #self.exe_js(self.js)
        self.type(self.billMonth,month)
        self.type(self.nameOrRoom,address)
        self.click(self.query_btn)

    #复选框
    checkboxs = 'xpath=>//table[@id="tb-feeBill"]/tbody/tr/td/span/input[@type="checkbox"]'
    #应缴金额
    pay_fee_eles = 'xpath=>//table[@id="tb-feeBill"]/tbody/tr/td[9]'
    #选中合计
    fee_count = 'id=>pay-fee-show'

    #缴费按钮
    pay_btn = 'id=>pay-button'

    #缴费人选择按钮
    select_btn = 'id=>ddl-btn-payerName'

    #缴费人名称
    payerName = 'xpath=>//ul[@id="payerName-ul-li-ul"]/li[1]/a'
    #发票抬头
    invoiceTitle = 'id=>invoiceTitle'
    #发票税号
    dutyParagraph = 'id=>dutyParagraph'
    #缴费人联系电话
    payerPhoneNumber = 'id=>payerPhoneNumber'
    #缴费确定按钮
    pay_confirm_btn = 'id=>edit-bill-button-confirm'

    def select_checkbox_items_sum_payFee(self):
        '''勾选复选框并计算合计金额'''
        checkboxes = self.find_elements(self.checkboxs)
        print(len(checkboxes))
        for checkbox in checkboxes:
            checkbox.click()
        fee_items = self.find_elements(self.pay_fee_eles)
        print(len(fee_items))
        sum_fee = 0
        for item in fee_items:
            fee = float(item.text)
            sum_fee += fee

        return sum_fee

    def get_count_fee(self):
        '''选中合计金额'''
        ele = self.find_element(self.fee_count)
        countFee = float(ele.text.split('元')[0])
        return countFee

    def do_payFee(self,invoiceTitle=None,dutyParagraph=None,payerPhoneNumber=None):
        '''缴费操作'''
        self.click(self.pay_btn)
        if invoiceTitle != None:
            self.type(self.invoiceTitle,invoiceTitle)
        self.click(self.select_btn)
        self.click(self.payerName)
        if dutyParagraph != None:
            self.type(self.dutyParagraph,dutyParagraph)
        if payerPhoneNumber != None:
            self.type(self.payerPhoneNumber,payerPhoneNumber)

        self.click(self.pay_confirm_btn)

    #关闭操作提示弹框
    close_btn = 'xpath=>//div[@id="error-div-modal-content"]/div/button[@type="button"]'

    def close_prompt(self):
        self.click(self.close_btn)




