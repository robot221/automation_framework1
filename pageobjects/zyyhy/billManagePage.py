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
        self.exe_js(self.js)
        self.type(self.billMonth,month)
        self.type(self.nameOrRoom,address)
        self.click(self.query_btn)

    #复选框
    checkboxs = 'xpath=>//input[@type="checkbox"]'
    #应缴金额
    pay_fee_eles = 'xpath=>//table[@id="tb-feeBill"]/tbody/tr/td[9]'
    #选中合计
    fee_count = 'id=>pay-fee-show'

    #缴费按钮
    pay_btn = 'id=>pay-button'

    #缴费人选择按钮
    select_btn = 'id=>ddl-btn-payerName'

