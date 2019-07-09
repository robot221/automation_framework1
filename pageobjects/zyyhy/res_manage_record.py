# -*- coding:utf-8 -*-

from framework.base_page import BasePage
class ResourceBookRecord(BasePage):
    #预约单号
    orderNo = 'id=>subOrderNo'
    #业主联系方式
    custPhone = 'id=>custPhone'
    #预订人联系方式
    reservationPhone = 'id=>reservationPhone'
    #创建开始时间
    orderStartTime = 'id=>orderStartTime'
    #创建结束时间：
    orderEndTime = 'id=>orderEndTime'
    #状态选择按钮
    btn_orderState = 'id=>ddl-btn-orderState'
    #状态列表
    orderStateOptions = 'xpath=>//ul[@id="orderState-ul-li-ul"]/li/a'
    #查询按钮
    query_btn = 'xpath=>//div[@id="public-edit-div-modal-body"]/div[@class="content-default"]/table/tbody/tr[2]/td[7]/button'

    #没有数据消息
    none_message = 'class_name=>mmg-message'
    #共有多少条数据
    totalCount = 'css=>div#pg_public_resource_order>div.totalCountLabel'
    #确定按钮
    button = 'css=>div.modal-footer.modal-footer0>a.btn.btn-primary.btn-modal0'

    #根据公共资源类型名称进行查询,返回数据量
    def query_by_orderNo(self,orderNo):
        self.type(self.orderNo,orderNo)
        self.click(self.query_btn)
        ele = self.find_element(self.totalCount)
        txt_content = ele.text
        num = txt_content.split('共')[1].split('条')[0]
        self.click(self.button)
        return num
