import os
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication

import getpass
password = getpass.getpass('Password : ')

message = EmailMessage()
message['Subject'] = 'Testing Subject'
message['From'] = 'jaeminbaek7023@gmail.com'
message['To'] = 'jbaek7023@naver.com'

message.set_content('''Email Content''')

message.add_alternative('''
    <h1>AskDjango VOD</h1>

    <img src="cid:f1.jpg" />

    <p>tag</p>
''', subtype='html')

filepath_list = ['./f1.jpg', './f2.jpg', './f3.jpg']
for filepath in filepath_list:
    with open(filepath, 'rb') as f:
        filename = os.path.basename(filepath)
        cid = filename
        img_data = f.read()
        part = MIMEApplication(img_data, name=filename)
        if cid == 'f1.jpg':
            part.add_header('Content-ID', '<' + cid + '>')
        else:
            part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % filename)
        message.attach(part)

with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
    server.ehlo()
    server.login('allieuslee', password)  # FIXME: 여러분의 네이버 계정명으로 변경해주세요.
    server.send_message(message)

print('Email Sent.')
