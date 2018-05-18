from pymysql import *

class MysqlHelper:
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self,sql,params=()):
        try:
            self.open()

            self.cursor.execute(sql,params)
            self.conn.commit()

            self.close()

            print('ok')
        except Exception as e:
            print(e.message)
