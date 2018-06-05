import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(STATIC_DIR, 'uploads')

class Config():
    DEBUG = True
    ENV = 'development'

    # 数据ku配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ROOT@192.168.80.135:3306/users'
    SQLALCHEMY_TRACK_MODIFICATION = False

    # 设置session相关参数
    SECRET_KEY = 'febhhfgbs$$%#dfsf'

    # 设置上传问价存放的位置



