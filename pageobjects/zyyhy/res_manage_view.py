# -*- coding:utf-8 -*-

from framework.base_page import BasePage
class ViewResource(BasePage):
    res_name = 'id=>resource_name-show'
    res_type = 'id=>resource_type-show'
    close_btn = 'xpath=>//div[@id="public-edit-div-modal-content"]/div/button[@class="close close0" and @type="button"]'

    #返回公共资源名称和类型
    def get_viewInfo(self):
        ele_name = self.find_element(self.res_name)
        name = ele_name.text
        ele_type = self.find_element(self.res_type)
        type = ele_type.text
        self.click(self.close_btn)
        return (name,type)