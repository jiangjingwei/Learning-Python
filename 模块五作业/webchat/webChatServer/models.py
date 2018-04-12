# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class User(Base):
#     # 表名称
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
#
# # 初始化数据库连接
# engine = create_engine("mysql+mysqldb://root:@localhose:3306/test?charset=utf8", echo=True)
# print(engine)
#
#
# DBSession = sessionmaker(bind=engine)
#
# session = DBSession()
# #
# new_user = User(id='5', name='alex')
#
# session.add(new_user)
# session.commit()
# session.close()

import pymysql


def login_check(user, pwd):

    conn = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql_varify = "select * from USER  WHERE username=%s and password=%s"

    result = cursor.execute(sql_varify, [user, pwd])

    conn.close()

    return result


def fetch_all_user():
    conn = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql_all_user = 'select * from USER '
    result_all = cursor.execute(sql_all_user)
    data_dict = cursor.fetchall()

    conn.close()
    return data_dict

