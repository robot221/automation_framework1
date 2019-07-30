# -*- coding;utf-8 -*-
from framework.base_page import BasePage
class ParkingNoticePage(BasePage):
    """
    园区公告管理页面
    """
    '''公共方法'''

    '''新增'''
    add_btn = 'id=>btn-add' #新增按钮
    systemName_btn = 'id=>ddl-btn-systemIdEdit' #选择项目下拉框按钮
    def select_systemName(self, systemName='请选择'):
        '''新增：选择项目'''
        if systemName != '请选择':
            self.click(self.systemName_btn)
            systemName_option = f'xpath=>//ul[@id="systemIdEdit-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
            if self.isElementExist(systemName_option):
                self.click(systemName_option)

    noticeTypeName_btn = 'id=>ddl-btn-noticeTypeName' #选择公告类型下拉框按钮
    def select_noticeTypeName(self, noticeTypeName='请选择'):
        '''新增：选择公告类型'''
        noticeTypeNames = ('活动','通知','紧急','新闻','知识','表扬')
        noticeTypeName_option = f'xpath=>//ul[@id="noticeTypeName-ul-li-ul"]/li/a[@itemtext="{noticeTypeName}"]'
        if noticeTypeName in noticeTypeNames:
            self.click(self.noticeTypeName_btn)
            self.click(noticeTypeName_option)

    noticeTitle = 'id=>noticeTitle' #公告名称输入框
    frame_id = 'ueditor_0'
    richText = 'tag=>body'
    save_btn = 'id=>edit-org-button-confirm'

    def type_richText(self,content):
        '''
        写入富文本框
        :param content: 公告内容
        :return:
        '''
        self.driver.switch_to.frame(self.frame_id)
        self.type(self.richText,content)
        self.driver.switch_to.default_content()

    close_alert_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-header modal-header"]/button[@class="close"]'#提示对话框关闭按钮
    def addNotice(self,systemName='中原壹号院',noticeTypeName='通知',noticeTitle='test',content='test'):
        '''
        新增公告
        :param systemName:项目名称
        :param noticeTypeName:公告类型
        :param noticeTitle:公告名称
        :param content:公告内容
        :return:
        '''
        self.click(self.add_btn)
        self.select_systemName(systemName)
        self.select_noticeTypeName(noticeTypeName)
        self.type(self.noticeTitle,noticeTitle)
        self.type_richText(content)
        self.click(self.save_btn)
        self.click(self.close_alert_btn)

    '''查询'''
    qsystemName_btn = 'id=>ddl-btn-projectName'  # 选择项目下拉框按钮

    def select_qsystemName(self, systemName='请选择'):
        '''查询：选择项目'''
        self.click(self.qsystemName_btn)
        systemName_option = f'xpath=>//ul[@id="projectName-ul-li-ul"]/li/a[@itemtext="{systemName}"]'
        if self.isElementExist(systemName_option):
            self.click(systemName_option)

    qnoticeTypeName_btn = 'id=>ddl-btn-qnoticeTypeName'  # 选择公告类型下拉框按钮

    def select_qnoticeTypeName(self, noticeTypeName='请选择'):
        '''新增：选择公告类型'''
        noticeTypeNames = ('请选择','活动', '通知', '紧急', '新闻', '知识', '表扬')
        noticeTypeName_option = f'xpath=>//ul[@id="qnoticeTypeName-ul-li-ul"]/li/a[@itemtext="{noticeTypeName}"]'
        if noticeTypeName in noticeTypeNames:
            self.click(self.qnoticeTypeName_btn)
            self.click(noticeTypeName_option)

    qName = 'id=>qName' #查询：公告名称输入框
    query_btn = 'id=>btn-query' #查询按钮

    def queryNotice(self,systemName='请选择',noticeTypeName='请选择',qName=None):
        '''
        查询公告
        :param systemName: 项目名称
        :param noticeTypeName: 公告类型
        :param qName: 公告标题
        :return:
        '''
        self.sleep(1)
        self.select_qsystemName(systemName)
        self.select_qnoticeTypeName(noticeTypeName)
        if qName:
            self.type(self.qName,qName)
        else:
            self.clear(self.qName)
        self.click(self.query_btn)

    totalCount = 'css=>div#pg>div.totalCountLabel'

    def get_totalCount(self):
        '''获取总记录数'''
        totalCount = self.find_element(self.totalCount).text.split('共')[1].split('条')[0]
        return int(totalCount)

    """
    修改
    """
    modify_btns = 'xpath=>//a[@class="calss-modify" and @title="修改"]' # 修改按钮

    def modifyNotice(self,noticeTypeName='通知',noticeTitle='modify',content='modify'):
        '''
        修改公告
        :param noticeTypeName: 公告类型
        :param noticeTitle: 公告标题
        :param content: 公告内容
        :return:
        '''
        if self.get_totalCount() > 0:
            modifyBtns = self.find_elements(self.modify_btns)
            modifyBtns[0].click()
            self.select_noticeTypeName(noticeTypeName)
            self.type(self.noticeTitle, noticeTitle)
            self.type_richText(content)
            self.click(self.save_btn)
            self.click(self.close_alert_btn)

    '''删除'''
    del_btns = 'xpath=>//a[@class="class-delete" and @title="删除"]'  # 删除按钮
    confirm_del_btn = 'xpath=>//div[@id="error-div-modal-content"]/div[@class="modal-footer modal-footer"]/a[1]'  # 确定删除按钮
    def delNotice(self):
        '''
        删除
        :return:
        '''
        if self.get_totalCount() > 0:
            delBtns = self.find_elements(self.del_btns)
            delBtns[-1].click()
            self.click(self.confirm_del_btn)
            self.click(self.close_alert_btn)