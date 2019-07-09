# -*- coding:utf-8 -*-
from framework.base_page import BasePage

class PldrPage(BasePage):
    add_button = "id=>add-button"
    btn_upload = "id=>btn-upload"
    btn_download = "id=>downTemplate"

    def updatefile(self):
        self.click(self.add_button)
        self.sleep(2)
        self.click(self.btn_upload)

    def downloadfile(self):
        self.click(self.add_button)
        self.sleep(2)
        self.click(self.btn_download)