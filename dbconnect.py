import pymysql as pm

class Database:
    def __init__(self):
        self.db=pm.connect('localhost','root','root','homeassist')
        self.cursor=self.db.cursor()

    def die(self):
        self.db.close()

    def storeLogin(self,name,email,passw1):

        self.sql="insert into storelogin values('"+name+"','"+email+"','"+passw1+"')"
        self.cursor.execute(self.sql)
        try:
            self.db.commit()
            self.status=True
        except:
            self.db.rollback()
            self.status = False
        return self.status

    def checkLogin(self,username,passw):

        self.sql="select * from login where email='"+username+"'\
            and password='"+passw+"'"
        self.cursor.execute(self.sql)
        if self.cursor.rowcount>0:
            self.status=True
        else:
            self.status=False
        return self.status