# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner
import time,os.path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
suites = unittest.TestLoader().discover("testunites",pattern="test_home*.py")

dir = os.path.dirname(os.path.abspath('.')) + '/templetes/'
rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
htmlFile = dir + rq + 'Html.html'

fp = open(htmlFile,'wb')

if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='项目测试报告',description='用例执行情况')
    runner.run(suites)
    fp.close()


    username = 'dxs86@163.com'
    password = 'dxs8806'
    receiver = ('282497745@qq.com','daixs@hicando.com')
    sender = 'dxs86@163.com'
    smtp_server = 'smtp.163.com'

    subject = '测试报告'

    msg = MIMEMultipart("mixed")
    msg['From'] = sender
    msg['To'] = ','.join(receiver)
    msg['Subject'] = Header(subject,'utf-8').encode()

    #邮件正文


    html = ''
    with open(htmlFile,'rb') as f:
        html = f.read()
    #print(f'hhhh:{html}')
    texthtml = MIMEText(html,'html','utf-8')
    texthtml["Content-Disposition"] = 'attachment; filename="testreport.html"'
    msg.attach(texthtml)

    imagedir = os.path.dirname(os.path.abspath('.')) + '/screenshots/20190420172805.png'
    with open(imagedir,'rb') as f:
        imagefile = f.read()
        image = MIMEImage(imagefile)
        image.add_header('Content-ID', '001')
        image['Content-Disposition'] = 'attachment; filename = "test.png"'
        msg.attach(image)

    text = '''
    <html>  
    <head></head>  
    <body>  
        <p>Hi!<br>  
            请查收测试报告！<br>  
            <img src="cid:001"> 
        </p> 
    </body>  
    </html>  
    '''
    textplain = MIMEText(text, 'html', 'utf-8')
    msg.attach(textplain)
    smtp = smtplib.SMTP_SSL(smtp_server,465)
    # smtp.starttls()
    smtp.set_debuglevel(1)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())