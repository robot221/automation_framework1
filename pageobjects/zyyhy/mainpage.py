# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class MainPage(BasePage):
    user_setting = 'id=>user_setting'

    menu_life = 'link_text=>智慧生活平台'

    menu_resource = 'link_text=>公共资源'
    #公共资源管理
    menu_res_manage = 'id=>accordion-item-290'
    #公共资源类型
    menu_res_type = 'id=>accordion-item-245'

    #社区邻里
    menu_neighbor = 'link_text=>社区邻里'

    #活动管理
    menu_active_m = 'id=>accordion-item-277'
    #投票管理
    menu_vote_m = 'id=>投票管理'


    def login_verify(self):
        ele = self.find_element(self.user_setting)
        return ele.text

    def click_menu_res_type(self):
        self.click(self.menu_life)
        self.move_to_ele(self.menu_resource)
        self.click(self.menu_res_type)

    def click_menu_res_manage(self):
        self.click(self.menu_life)
        self.move_to_ele(self.menu_resource)
        self.click(self.menu_res_manage)

    #跳转到活动管理
    def click_menu_active_m(self):
        #self.sleep(5)
        self.click(self.menu_life)
        self.move_to_ele(self.menu_neighbor)
        self.click(self.menu_active_m)

    #跳转到投票管理
    def click_menu_vote_m(self):
        self.click(self.menu_life)
        self.move_to_ele(self.menu_neighbor)
        self.click(self.menu_vote_m)

    menu_xsjf = 'link_text=>线上缴费'
    #账单批量导入
    zdpldr = 'id=>accordion-item-237'
    #账单管理
    zdgl = 'id=>accordion-item-236'
    #缴费信息报表
    jfxxbb = 'id=>accordion-item-296'
    #物业收费标准
    wysfbz = 'id=>accordion-item-291'
    #停车费代缴
    tcfdj = 'id=>accordion-item-274'
    #缴费二维码
    jfewm = 'id=>accordion-item-297'


    def click_zdpldr(self):
        '''跳转到账单批量导入'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_xsjf)
        self.click(self.zdpldr)

    def click_zdgl(self):
        '''跳转到账单管理'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_xsjf)
        self.click(self.zdgl)

    def click_jfxxbb(self):
        '''跳转到缴费信息报表'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_xsjf)
        self.click(self.jfxxbb)


    def click_wysfbz(self):
        '''跳转到物业收费标准'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_xsjf)
        self.click(self.wysfbz)


    def click_tcfdj(self):
        '''跳转到停车费代缴'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_xsjf)
        self.click(self.tcfdj)


    def click_jfewm(self):
        '''跳转到缴费二维码'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_xsjf)
        self.click(self.jfewm)

    menu_yjlx = 'link_text=>一键联系'
    lxrgl = 'id=>accordion-item-249' #联系人管理
    bdjl = 'id=>accordion-item-294' #拨打记录

    def click_lxrgl(self):
        '''跳转到联系人管理'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_yjlx)
        self.click(self.lxrgl)

    def click_bdjl(self):
        '''跳转到拨打记录'''
        self.click(self.menu_life)
        self.move_to_ele(self.menu_yjlx)
        self.click(self.bdjl)

    menu_base = 'link_text=>基础平台'
    menu_device = 'link_text=>设备档案'
    deviceManage = 'id=>accordion-item-275' #设备档案
    def click_deviceManage(self):
        '''跳转到设备档案'''
        self.click(self.menu_base)
        self.move_to_ele(self.menu_device)
        self.click(self.deviceManage)

    menu_project = 'link_text=>项目管理'
    projectManage = 'id=>accordion-item-264' #项目管理
    def click_projectManage(self):
        '''跳转到项目管理'''
        self.click(self.menu_base)
        self.move_to_ele(self.menu_project)
        self.click(self.projectManage)

    menu_os = 'link_text=>物业运营平台'
    menu_express = 'link_text=>快递信息'
    expressInfoM = 'id=>accordion-item-239' #快递信息管理
    def click_expressInfoM(self):
        '''跳转到快递信息管理'''
        self.click(self.menu_os)
        self.move_to_ele(self.menu_express)
        self.click(self.expressInfoM)

    menu_parkingNotice = 'link_text=>园区公告'
    parkingNoticeM = 'id=>accordion-item-243' #园区公告管理
    def click_parkingNoticeM(self):
        '''跳转到园区公告管理'''
        self.click(self.menu_os)
        self.move_to_ele(self.menu_parkingNotice)
        self.click(self.parkingNoticeM)




