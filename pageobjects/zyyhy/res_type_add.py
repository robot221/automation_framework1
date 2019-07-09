# -*- coding: utf-8 -*-

from framework.base_page import BasePage

class ResTypeAdd(BasePage):
    #类型名称输入框
    resTypeName_input = 'id=>qresourceTypeName'
    #选择项目下拉框按钮
    systemName_btn = 'id=>ddl-btn-resTypeSystemName'
    #中原壹号院选项
    zyyhy_option = 'link_text=>中原壹号院'
    #描述输入框
    des_input = 'id=>qdescription'

    #确定按钮
    confirm_btn = 'id=>resourceType-edit-button-confirm'

    #新增资源类型
    def add_res_type(self,typeName,des=''):
        self.type(self.resTypeName_input,typeName)
        self.click(self.systemName_btn)
        self.click(self.zyyhy_option)
        if len(des) > 0:
            self.type(self.des_input,des)

        self.click(self.confirm_btn)