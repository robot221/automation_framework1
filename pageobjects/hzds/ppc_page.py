# -*- coding:utf-8 -*-
from framework.base_page import BasePage

class PPCPage(BasePage):
    '''
    巡更点分类页面
    '''
    #新增按钮
    add_btn = 'id=>btn-add'
    #查询按钮
    query_btn = 'id=>btn-query'
    #显示项目选项按钮
    pro_name_btn = 'id=>ddl-btn-projectName'

    #第一个项目选项
    fir_pro_name = 'xpath=>//ul[@id="projectName-ul-li-ul"]/li[1]'

    #记录数元素
    result_num = 'xpath=>//div[@id="pg"]/div/span'

    #修改按钮
    edit_btn = 'xpath=>//table[@id="tb_catagorys"]/tbody/tr[1]/td[5]/span/a[1]'
    #删除按钮
    del_btn = 'xpath=>//table[@id="tb_catagorys"]/tbody/tr[1]/td[5]/span/a[2]'

    #一级分类输入框
    firstLevelNameInput = 'id=>firstLevelName'
    #二级分类输入框
    secondLevelNameInput = 'id=>secondLevelName'

    #点击新增按钮操作，弹窗
    def add_btn_click(self):
        self.click(self.add_btn)

    #查询操作
    def query_btn_click(self):
        self.click(self.query_btn)

    #判断第一个选项是请选择
    def is_fir_pro_name(self,text):
        flag = False
        self.click(self.pro_name_btn)
        ele = self.find_element(self.fir_pro_name)
        if ele.is_displayed() and ele.text == text:
            flag =  True
        return flag

    #输入一级分类
    def input_firstLevel(self,text):
        self.type(self.firstLevelNameInput,text)

    # 输入二级分类
    def input_secondLevel(self, text):
        self.type(self.secondLevelNameInput, text)

    #获取结果数量
    def get_resultNum(self):
        ele = self.find_element(self.result_num)
        num = ele.text
        return int(num)

    #点击修改按钮操作
    def edit_btn_click(self):
        if self.get_resultNum() > 0:
            self.click(self.edit_btn)

    #点击删除按钮操作
    def del_btn_click(self):
        if self.get_resultNum() > 0:
            self.click(self.del_btn)


