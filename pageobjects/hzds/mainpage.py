# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class MainPage(BasePage):
    dzxg_menu = "xpath=>//*[@id='div-menu-object-accordion']/ul/li[4]/a"
    #父节点
    dzxg_parent_node = "xpath=>//*[@id='div-menu-object-accordion']/ul/li[4]"
    #巡更点分类
    xgdfl_menu = "link_text=>巡更点分类"
    #巡更点内容
    xgdnr_menu = "link_text=>巡更点内容"
    # 巡更点位置
    xgdwz_menu = "link_text=>巡更点位置"
    # 巡更点管理
    xgdgl_menu = "link_text=>巡更点管理"
    # 巡更路线管理
    xglxgl_menu = "link_text=>巡更路线管理"
    # 巡更路线执行明细
    xglxzxmx_menu = "link_text=>巡更路线执行明细"
    # 巡更数据批量导入
    xgsjpldr_menu = "link_text=>巡更数据批量导入"

    #登录成功元素
    user_messages = "xpath=>//*[@id='user-messages']/a"

    def click_dzxg(self):
        ele_dzxg = self.find_element(self.dzxg_menu)
        attr = ele_dzxg.get_attribute("href")
        print(attr)
        ele_dzxg.click()

        ele_parent = self.find_element(self.dzxg_parent_node)
        class_value = ele_parent.get_attribute("class")
        return class_value

    def click_xgdfl_menu(self):
        if self.click_dzxg() == 'submenu open':
            self.click(self.xgdfl_menu)

    def click_xgsjpldr_menu(self):
        if self.click_dzxg() == 'submenu open':
            self.click(self.xgsjpldr_menu)

    def get_user_message(self):
        ele_um = self.find_element(self.user_messages)
        text = ele_um.text
        return text