# -*- coding ; utf-8 -*-

from framework.base_page import BasePage

class ResManagePage(BasePage):
    #查询按钮
    query_btn = 'xpath=>//div[@id="content-page"]/div/table/tbody/tr[2]/td[7]/button[1]'
    #新增按钮
    add_btn = 'xpath=>//div[@id="content-page"]/div/table/tbody/tr[2]/td[7]/button[2]'

    #查询条件 资源名称输入框
    resName_input = 'id=>resourceName'

    #修改按钮列表
    modify_btn_list = 'class=>calss-modify'
    #删除按钮列表
    del_btn_list = 'class=>class-delete'
    #预览按钮列表
    view_btn_list = 'xpath=>//a[@class="class-eye" and @title="预览"]'
    #预定记录按钮列表
    record_btn_list = 'xpath=>//a[@class="class-eye" and @title="预订记录"]'

    #按资源名称查询
    def search_byName(self,resname):
        self.type(self.resName_input,resname)
        self.click(self.query_btn)

    #进入新增对话框
    def click_add_dialog(self):
        self.click(self.add_btn)

    #打开修改页面
    def click_modify_dialog(self):
        eles = self.find_elements(self.modify_btn_list)
        if len(eles) > 0:
            eles[0].click()

    #点击删除按钮
    def click_delete_btn(self):
        eles = self.find_elements(self.del_btn_list)
        if len(eles) > 0:
            eles[0].click()

    #打开预览页面
    def click_view_dialog(self):
        eles = self.find_elements(self.view_btn_list)
        if len(eles) > 0:
            eles[0].click()

    #打开预订记录页面
    def click_record_dialog(self):
        eles = self.find_elements(self.record_btn_list)
        if len(eles) > 0:
            eles[0].click()

