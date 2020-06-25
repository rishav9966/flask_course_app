import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x00\x9b1\xc6\xc4mu?\x06\x046\x88\x8a\x00\x87H'
    
    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}

