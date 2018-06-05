from flask_sqlalchemy import SQLAlchemy, BaseQuery

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)


def query(cls) -> BaseQuery:  # 通过->来声明函数返回的类型
    return db.session.query(cls)


def queryAll(cls):
    return query(cls).all()


def add(obj):  # 更新和添加
    db.session.add(obj)
    db.session.commit()


def delete(obj):
    db.session.delete(obj)
    db.session.commit()


def queryById(cls, id):  # 根据id查找数据
    return query(cls).get(int(id))


def deleteById(cls, id):
    try:
        obj = queryById(cls, id)
        delete(obj)
        return True
    except:
        pass
    return False
