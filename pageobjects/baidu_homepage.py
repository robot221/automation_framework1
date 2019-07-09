# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class BaiduHomepage(BasePage):
    search_input = 'id=>kw'
    button = 'id=>su'

    def type_search(self,text):
        self.type(self.search_input,text)
    def submit_button(self):
        self.click(self.button)
