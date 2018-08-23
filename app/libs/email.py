from flask import current_app, render_template

from app import mail
from flask_mail import Message


# 发送电子邮件
def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1572926321@qq.com',
    #               body='zzxun 的测试邮件',
    #               recipients=['zhangzhaoxun@outlook.com'])
    msg = Message('[ZZXUN]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
