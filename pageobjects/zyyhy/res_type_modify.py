# -*- coding: utf-8 -*-

from framework.base_page import BasePage

class ResTypeModify(BasePage):
    #类型名称输入框
    resTypeName_input = 'id=>qresourceTypeName'
    #描述输入框
    des_input = 'id=>qdescription'

    #确定按钮
    confirm_btn = 'id=>resourceType-edit-button-confirm'

    #修改资源类型
    def modify_res_type(self,typeName='',des=''):
        if len(typeName) > 0:
            self.type(self.resTypeName_input,typeName)
        if len(des) > 0:
            self.type(self.des_input,des)
        self.click(self.confirm_btn)
