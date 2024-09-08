# import pymysql
# class Database():
#     def __init__(self):
#         self.db=pymysql.connect(host='lacalhost',
#                                 user='root',
#                                 password='your password',
#                                 db='your_dbname',
#                                 charset='utf8')
#         self.cursor = self.db.cursor(pymysql.cursor.DictCursor)
    
#     def execute(self, query, args={}):
#         self.cursor.execute(query, args)
    
#     def executeOne(self, query, args={}):
#         self.cursor.execute(query, args)
#         row = self.cursor.fetchone()
#         return row
    
#     def executeAll(self, query, args={}):
#         self.cursor.execute(query, args)
#         row=self.cursor.fetchall()
#         return row


#     def commit():
#         self.db.commit() 
# 모듈 import
import pymysql


# MySQL 데이터베이스 연결
db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='shop', charset='utf8')

# 데이터에 접근
cursor = db.cursor()

# SQL query 작성
sql = "select * from users"

# SQL query 실행
cursor.execute(sql)

# db 데이터 가져오기
cursor.fetchall() #모든 행 가져오기
cursor.fetchone() # 하나의 행만 가져오기
cursor.fetchmany(n) # n개의 데이터 가져오기 

# 수정 사항 db에 저장
db.commit()
 
# Database 닫기
db.close()