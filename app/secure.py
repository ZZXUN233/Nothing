"""
    Created by ZZXUN on 2018/8/6
"""

__author__ = "ZZXUN"
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root@localhost:3306/poem'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECRET_KEY = "dFDLEIGNDsdgkerto195h83i72hs723u48/?dg14s."
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# Email 配置

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1572926321@qq.com'
MAIL_PASSWORD = 'qnwytahushmeiieb'
MAIL_SUBJECT_PREFIX = '[打扰了]'
MAIL_SENDER = 'ZZXUN<zzxun.cn>'
