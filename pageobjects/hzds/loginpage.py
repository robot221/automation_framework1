# -*- coding:utf-8 -*-

from framework.base_page import BasePage

class LoginPage(BasePage):
    username = "id=>username"
    passwd = "id=>password"
    submit_btn = "id=>submit-btn"

    def login(self,user,password):
        self.type(self.username,user)
        self.type(self.passwd,password)
        self.click(self.submit_btn)