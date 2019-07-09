# -*- coding; utf-8 -*-

from framework.base_page import BasePage
from pywinauto import application  #Spy++

class ModifyResource(BasePage):
    #资源名称输入框
    resName_input = 'id=>resource_name-edit'
    #地址
    address_input = 'id=>address_edit'
    #电话
    phone_input = 'id=>phone_number'
    #添加资源图片按钮
    addImg_btn = 'id=>addImg'
    #资源描述文本框
    resourceDesc_area = 'id=>resourceDesc'
    #生效时间输入框
    validDate_input = 'id=>validDate'
    #失效时间输入框
    expireDate_input = 'id=>expireDate'
    #确定按钮
    confirm_btn = 'id=>public-edit-div-button-confirm'

    #资源配置项
    res_conf_id = 'id=>"organize_attribute_group_id'
    #资源配置输入框
    res_conf_inputs = 'xpath=>//tr[@id="organize_attribute_group_id"]/td/input'

    #输入资源配置
    def type_res_config(self,content='无'):
        if self.isElementExist(self.res_conf_id):
            eles = self.find_elements(self.res_conf_inputs)
            for ele in eles:
                self.type(ele,content)
        else:
            print("不存在资源配置项")

    #上传资源图片
    def upload_resImg(self,imgUrl):
        self.click(self.addImg_btn)
        self.sleep(2)
        app = application.Application()
        app.connect(title=u'打开', class_name='#32770')
        window = app.window(title=u'打开', class_name='#32770')
        # 文件所在路径不能含有空格
        window["Edit"].type_keys(imgUrl)
        self.sleep(2)
        window["ScrollBar"].click()
        window[u"打开(O)"].click()
        self.sleep(2)

    #修改公共资源
    def modify_resource(self,resName,address,phone,imgUrl,resDesc,validDate,expireDate):
        '''修改公共资源，参数为：资源名称，地址，电话，资源图片地址，资源描述，生效时间，失效时间'''
        self.type(self.resName_input, resName)  # 输入资源名称
        self.type(self.address_input,address) #输入地址
        self.type(self.phone_input,phone) #输入电话
        self.upload_resImg(imgUrl) #上传资源图片
        self.type_res_config() #资源配置
        self.type(self.resourceDesc_area,resDesc) #输入资源描述
        self.type(self.validDate_input,validDate) #输入生效时间
        self.type(self.expireDate_input,expireDate) #输入失效时间
        self.sleep(1)
        self.click(self.confirm_btn)

