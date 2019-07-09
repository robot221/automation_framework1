# -*- coding:utf-8 -*-
from framework.base_page import BasePage

class PpcAddPage(BasePage):
    """
    新增巡更点分类
    """
    #所属项目元素
    #下拉框弹出按钮
    btn_eprojectName = "id=>ddl-btn-eprojectName"
    #总元素
    pronames = "xpath=>//*[@id='eprojectName-ul-li-ul']/li"
    #第一个选项
    f_proname = "xpath=>//*[@id='eprojectName-ul-li-ul']/li[1]/a"
    #第二个选项
    s_proname = "xpath=>//*[@id='eprojectName-ul-li-ul']/li[2]/a"

    #分类级别
    #下拉框弹出按钮
    btn_elevelName = "id=>ddl-btn-elevelName"
    #总选项
    elevelNames = "xpath=>//*[@id='elevelName-ul-li-ul']/li"
    #一级分类
    f_elevelName = "xpath=>//*[@id='elevelName-ul-li-ul']/li[1]/a"
    # 二级分类
    s_elevelName = "xpath=>//*[@id='elevelName-ul-li-ul']/li[2]/a"

    #上级级别
    #下拉框弹出按钮
    btn_eparentName = "id=>ddl-btn-eparentName"
    #总选项
    eparentNames = "xpath=>//*[@id='eparentName-ul-li-ul']/li/a"
    #第一个选项
    f_eparentName = "xpath=>//*[@id='eparentName-ul-li-ul']/li[1]/a"
    #最后一个选项
    end_eparentName = "xpath=>//*[@id='eparentName-ul-li-ul']/li[-1]/a"

    #类别名称
    input_name = "id=>name"
    #备注
    remark = "id=>remark"

    #确定按钮
    submit_btn = "id=>operate-div-button-confirm"

    #操作成功弹框div
    div = "id=>error-div-modal-content"

    #操作成功说明元素
    div_content = "xpath=>//div[@id='error-div-modal-content']/div[@class='modal-body']/div"

    #操作成功弹框确认按钮
    div_btn = "xpath=>//div[@id='error-div-modal-content']/div[@class='modal-footer modal-footer']/a"

    def get_eprojectName_num(self):
        """项目列表数量"""
        #self.click(self.btn_eprojectName)
        eles = self.find_elements(self.pronames)
        #print(eles)
        return len(eles)


    def is_fir_pro_name(self):
        """判断第一个选项是请选择"""
        flag = False
        self.click(self.btn_eprojectName)
        #self.sleep(2)
        ele = self.find_element(self.f_proname)
        #self.sleep(2)
        #print(ele.is_displayed())
        #print(f"ele.text:{ele.text}")
        if ele.is_displayed() and ele.text == "请选择":
            #print("true")
            flag = True
        return flag

    def select_pro_name(self):
        """选择项目"""
        if self.is_fir_pro_name():
            #ele = self.find_element(self.s_proname)
            #itemdata = ele.get_attribute("itemdata")
            #itemtext = ele.get_attribute("itemtext")
            #print(itemdata,itemtext)
            self.click(self.s_proname)
            #js = f'''
            #//document.getElementById("eprojectName").value="{itemtext}";
            #//document.getElementById("eprojectVal").value="{itemdata}";
            #alert("{itemtext},{itemdata}");
            #'''
            #self.driver.execute_script(js)



    def get_elevelNames_num(self):
        """分类级别数量"""
        eles = self.find_elements(self.elevelNames)
        return len(eles)

    def select_s_elevelName(self):
        """选择二级分类"""
        self.click(self.btn_elevelName)
        self.click(self.s_elevelName)

    def select_eparentName(self):
        """选择上级级别"""
        self.click(self.btn_eparentName)
        eles = self.find_elements(self.eparentNames)
        #print(eles[-1].text)
        eles[-1].click()
        #self.click(self.end_eparentName)

    def type_name(self,name,remark):
        """输入类别名称，备注"""
        self.type(self.input_name,name)
        self.type(self.remark,remark)

    def submit_click(self):
        self.click(self.submit_btn)

    def get_succ_text(self):
        ele = self.find_element(self.div_content)
        text = ele.text
        print(text)
        return text

    def click_div_btn(self):
        self.click(self.div_btn)