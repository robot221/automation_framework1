# -*- coding:utf-8 -*-
from framework.base_page import BasePage
from pywinauto import application  #Spy++
class ProjectBannerPage(BasePage):
    '''
    项目轮播图
    '''
    """新增轮播图"""
    add_btn = 'id=>btn-add-banner' #新增按钮
    add_img_btn = 'id=>bannerImage' #新增图片按钮


    def upload(self, filePath):
        """
        上传图片
        :param filePath: 图片路径
        :return:
        """
        self.sleep(1)
        app = application.Application()
        app.connect(title=u'打开', class_name='#32770')
        window = app.window(title=u'打开', class_name='#32770')
        # 文件所在路径不能含有空格
        window["Edit"].type_keys(filePath)
        self.sleep(2)
        window["ScrollBar"].click()
        window[u"打开(O)"].click()
        self.sleep(2)

    contentName = 'id=>contentName' #图片名称输入框
    description = 'id=>description' #图片描述输入框
    appType_btn = 'id=>ddl-btn-appTypeInputName' #选择app类型按钮
    def select_appType(self,appType):
        '''
        选择app类型
        :param appType: APP类型
        :return:
        '''
        appTypes = ('项目首页图片','臻心汇APP')
        appType_option = f'xpath=>//ul[@id="appTypeInputName-ul-li-ul"]/li/a[@itemtext="{appType}"]'
        if appType in appTypes:
            self.click(self.appType_btn)
            self.click(appType_option)
    save_btn = 'id=>project-edit-banner-button-confirm' #保存确定按钮
    close_alert_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-header modal-header"]/button[@class="close"]'  # 提示对话框关闭按钮

    def addBanner(self,imgUrl,contentName,description,appType='项目首页图片'):
        """
        添加banner图
        :param imgUrl: 图片路径
        :param contentName: 图片名称
        :param description: 图片描述
        :param appType: app类型
        :return:
        """
        self.click(self.add_btn)
        self.upload(imgUrl)
        self.type(self.contentName,contentName)
        self.type(self.description,description)
        self.select_appType(appType)
        self.click(self.save_btn)
        self.click(self.close_alert_btn)

    """查询"""
    qAppType = 'id=>ddl-btn-qAppTypeId' # 查询条件：选择app类型按钮
    def select_qAppType(self,appType):
        '''
        选择app类型
        :param appType: APP类型
        :return:
        '''
        appTypes = ('项目首页图片','臻心汇APP')
        appType_option = f'xpath=>//ul[@id="qAppTypeId-ul-li-ul"]/li/a[@itemtext="{appType}"]'
        if appType in appTypes:
            self.click(self.qAppType)
            self.click(appType_option)

    query_btn = 'id=>btn-query-banner' #查询按钮

    def queryBanner(self,appType='请选择'):
        """
        查询
        :param appType:
        :return: app类型
        """
        self.select_qAppType(appType)
        self.click(self.query_btn)

    totalCount = 'css=>div#pageLabel>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)