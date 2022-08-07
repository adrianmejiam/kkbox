import sqlite3

class Connect():
    def __init__(self):
        self.connect = sqlite3.connect('.\\Demo\\app\\dbs\\mydatabase.db')
        self.cursor = self.connect.cursor()
        #self.cursor.execute("SELECT VERSION()")
        #data = self.cursor.fetchone()
        #print ("Database version : %s " % data)

    def createTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS testpymysql2")
        sql = """CREATE TABLE testpymysql2 (\
                FIRST_NAME TEXT,\
                LAST_NAME  TEXT,\
                AGE INT,\
                SEX TEXT(1),\
                INCOME INT)"""
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print("--創建表成功--")
        except:
            print("--創建表失敗--")
            self.connect.rollback()

    def insertTable(self):
        sql = """INSERT INTO testpymysql2(FIRST_NAME,\
            LAST_NAME, AGE, SEX, INCOME)\
            VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print("--新增成功--")
        except:
            print("--新增失敗--")
            self.connect.rollback()
    

    def deleteTable(self):
        sql = "DELETE FROM testpymysql2 WHERE AGE >= %s and SEX = '%c'" % (20, 'M')
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print("--刪除成功--")
        except:
            print("--刪除失敗--")
            self.connect.rollback()

    def updateTable(self):
        sql = "UPDATE testpymysql2 SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print("--更新成功--")
        except:
            print("--更新失敗--")
            self.connect.rollback()

    def selectTable(self):
        sql = "SELECT * FROM testpymysql2"
        try:
            self.cursor.execute(sql)
            datas = self.cursor.fetchall()
            print("--查詢成功--")
            for index, data in enumerate(datas):
                fname = data[0]
                lname = data[1]
                age = data[2]
                sex = data[3]
                income = data[4]
                print ("%s:fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                    (index, fname, lname, age, sex, income ))
            
        except:
            print(555)
            self.connect.rollback()

if __name__ == '__main__':
    ct = Connect()
    ct.insertTable()
    ct.updateTable()
    ct.selectTable()
    ct.connect.close()
