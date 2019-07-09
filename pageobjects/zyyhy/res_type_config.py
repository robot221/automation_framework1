# -*- coding; utf-8 -*-
from framework.base_page import BasePage

class ResTypeConfig(BasePage):
    #新增按钮
    addConfigItem_btn = 'id=>addConfigItem'
    #确定按钮
    saveConfig_btn = 'id=>saveConfig'
    #配置编码1
    paramCode_1 = 'id=>paramCode_1'

    #配置名称1
    paramName_1 = 'id=>paramName_1'

    # 操作提示
    opt_message = 'css=>div#error-div-modal-content>div.modal-body'

    # 操作提示按钮
    opt_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[3]/a'
    #新增配置
    def add_config(self,paramcode,paramname):
        self.click(self.addConfigItem_btn)
        self.type(self.paramCode_1,paramcode)
        self.type(self.paramName_1,paramname)
        self.click(self.saveConfig_btn)
    #修改配置
    def modify_config(self,paramcode,paramname):
        #self.click(self.addConfigItem_btn)
        self.type(self.paramCode_1, paramcode)
        self.type(self.paramName_1, paramname)
        self.click(self.saveConfig_btn)


    #得到操作消息并关闭操作提示弹窗
    def get_opt_message(self):
        ele = self.find_element(self.opt_message)
        message = ele.text
        #print('message:',message)
        self.click(self.opt_btn)
        return message