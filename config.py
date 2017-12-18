import os
# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = b'\xd6\xb3\x18\xed\x84\x8b\xfc\t\xaamW\xe0\x9c\x07\xfd\xc7\xbf\x1cW\x9dm\xaa>\x8b'
    SQLALCHEMY_DATABASE_URI = "postgres://wkikkpvhhsfhda:4b041766d1f68c5aee188e0c080c1eb1d39bbd3459503c19adea89863ecb5a43@ec2-54-235-244-185.compute-1.amazonaws.com:5432/d1tf3le2r6ka19"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print(SQLALCHEMY_DATABASE_URI)

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
