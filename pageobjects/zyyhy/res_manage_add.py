# -*- coding; utf-8 -*-

from framework.base_page import BasePage
from pywinauto import application  #Spy++
class ResMngAddPage(BasePage):
    #项目名称下拉框按钮
    sSystemName_btn = 'id=>ddl-btn-sSystemName'
    # 中原壹号院选项
    zyyhy_option = 'link_text=>中原壹号院'
    #资源名称输入框
    resName_input = 'id=>resource_name-edit'
    #资源类型下拉框按钮
    resType_btn = 'id=>ddl-btn-resourceTypeEdit'
    #资源类型列表
    resTypes = 'xpath=>//ul[@id="resourceTypeEdit-ul-li-ul"]/li/a'
    #地址
    address_input = 'id=>address_edit'
    #电话
    phone_input = 'id=>phone_number'
    #资源通道列表
    passages = 'xpath=>//div[@id="passageChannel"]/span/label/div/span/input'
    #添加资源图片按钮
    addImg_btn = 'id=>addImg'
    #预定类型时间
    session_type_time = 'xpath=>//div[class="row_show"]/label/input[@value="2"]'
    # 预定类型场次
    session_type_cc = 'xpath=>//div[class="row_show"]/label/input[@value="1"]'
    #添加预定按钮
    add_resSession_btn = 'id=>addResourceSession'
    #场次名称输入框
    sessionName_input = 'id=>inputSessionName'
    #预定开始时间输入框
    selectStartTime = 'id=>selectStartTime'
    #预定开始时间选择列表
    startTime_list = 'xpath=>//div[@id="datetimepicker-startTime"]/div/div/div/div[@class="xdsoft_time "]'
    #预定结束时间输入框
    selectEndTime = 'id=>selectEndTime'
    # 预定结束时间选择列表
    endTime_list = 'xpath=>//div[@id="datetimepicker-endTime"]/div/div/div/div[@class="xdsoft_time "]'
    #时间段类型列表
    selectWeeklist = 'name=>selectWeek'
    #预定确认按钮
    add_session_confirm_btn='id=>add-session-div-button-confirm'
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
    def type_res_config(self,content='有'):
        if self.isElementExist(self.res_conf_id):
            eles = self.find_elements(self.res_conf_inputs)
            for ele in eles:
                self.type(ele,content)
        else:
            print("不存在资源配置项")

    #选择指定的资源类型
    def select_resType(self,typeName):
        '''选择指定的资源类型'''
        self.click(self.resType_btn)
        type_eles = self.find_elements(self.resTypes)
        flag = True
        for ele in type_eles:
            if ele.text == typeName:
                ele.click()
                flag = False
                break
        if flag:
            print(f'不存在资源类型{typeName}')

    #勾选指定数量的资源通道，若小于指定数量则勾选全部
    def select_passages(self,num):
        eles = self.find_elements(self.passages)
        if len(eles) <= num:
            for ele in eles:
                ele.click()
        if len(eles) > num:
            for i in range(num):
                eles[i].click()

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

    #选择开始时间
    def select_startTime(self,startTime):
        self.click(self.selectStartTime)
        eles = self.find_elements(self.startTime_list)
        for ele in eles:

            print(ele.text)
            if ele.text == startTime:
                ele.click()
                break

    #选择结束时间
    def select_endTime(self,endTime):
        self.click(self.selectEndTime)
        eles = self.find_elements(self.endTime_list)
        for ele in eles:
            if ele.text == endTime:
                ele.click()
                break

    #勾选指定数量的时间段，若小于指定数量则勾选全部
    def select_weeks(self,num):
        eles = self.find_elements(self.selectWeeklist)
        if len(eles) <= num:
            for ele in eles:
                ele.click()
        if len(eles) > num:
            for i in range(num):
                eles[i].click()
    #增加预定类型
    def add_resSession(self,startTime,endTime,sessionType='时间',weeknum=7,sessinName=None):
        if sessionType == '时间':
            self.click(self.add_resSession_btn)
        else:
            self.click(self.session_type_cc)
            self.click(self.add_resSession_btn)
            self.type(self.sessionName_input,sessinName)
        #self.select_startTime(startTime)
        self.type(self.selectStartTime,startTime)
        #self.select_endTime(endTime)
        self.type(self.selectEndTime,endTime)
        self.select_weeks(weeknum)
        self.click(self.add_session_confirm_btn)

    def add_resource(self,resName,typeName,address,phone,passnum,imgUrl,resDesc,validDate,expireDate,startTime,endTime,sessionType='时间',weeknum=7,sessinName=None):
        '''添加公共资源，参数为：资源名称，资源类型，地址，电话，资源通道数量，资源图片地址，资源描述，生效时间，失效时间，预定开始时间，预定结束时间，预定类型，预定时间段数量，场次名称'''
        self.click(self.sSystemName_btn) #点击选择项目按钮
        self.click(self.zyyhy_option) #选择中原壹号院项目

        self.type(self.resName_input,resName) #输入资源名称
        self.select_resType(typeName) #选择资源类型
        self.type(self.address_input,address) #输入地址
        self.type(self.phone_input,phone) #输入电话
        self.select_passages(passnum) #勾选资源通道
        self.upload_resImg(imgUrl) #上传资源图片
        self.type_res_config() #资源配置
        self.add_resSession(startTime,endTime) #增加预定类型
        self.type(self.resourceDesc_area,resDesc) #输入资源描述
        self.type(self.validDate_input,validDate) #输入生效时间
        self.type(self.expireDate_input,expireDate) #输入失效时间
        self.sleep(3)
        self.click(self.confirm_btn)

