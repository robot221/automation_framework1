# -*- coding: utf-8 -*-

from framework.base_page import BasePage

class ResType(BasePage):
    #新增按钮
    add_btn = 'id=>btn-add-resourceType'
    #查询按钮
    query_btn = 'id=>btn-query-resourceType'
    #修改按钮
    modify_btn = 'class_name=>calss-modify'
    #删除按钮
    del_btn = 'class_name=>calss-delete'
    #配置按钮
    plus_btn = 'class_name=>calss-plus'
    #查看按钮
    view_btn = 'class_name=>query-config'

    #资源名称输入框
    typename_input = 'id=>resourceTypeName'
    #没有数据元素
    none_message = 'class_name=>mmg-message'
    #共有多少条数据元素
    totalCount = 'css=>div.totalCountLabel'

    #确定删除按钮
    confirm_del_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[3]/a[1]'

    # 操作提示
    opt_message = 'css=>div#error-div-modal-content>div.modal-body'

    # 操作提示按钮
    opt_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[3]/a'

    #打开新增页面
    def click_add_btn(self):
        self.click(self.add_btn)

    #打开修改页面
    def click_modify_btn(self):
        eles = self.find_elements(self.modify_btn)
        if len(eles) > 0:
            eles[0].click()

    #删除
    def click_del_btn(self):
        eles = self.find_elements(self.del_btn)
        if len(eles) > 0:
            eles[0].click()

    #配置
    def click_plus_btn(self):
        eles = self.find_elements(self.plus_btn)
        if len(eles) > 0:
            eles[0].click()

    #查看
    def click_view_btn(self):
        eles = self.find_elements(self.view_btn)
        if len(eles) > 0:
            eles[0].click()

    #根据公共资源类型名称进行查询,返回数据量
    def query_by_name(self,name):
        self.type(self.typename_input,name)
        self.click(self.query_btn)
        ele = self.find_element(self.totalCount)
        txt_content = ele.text
        num = txt_content.split('共')[1].split('条')[0]
        return num

    #删除公共资源类型
    def del_res_type(self):
        self.click_del_btn()
        self.click(self.confirm_del_btn)

    #得到操作消息并关闭操作提示弹窗
    def get_opt_message(self):
        ele = self.find_element(self.opt_message)
        message = ele.text
        #print('message:',message)
        self.click(self.opt_btn)
        return message


