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

