from flask import request, render_template
import PyMySQL

def index():
	if request.method =='POST':
		if request.values['send']=='送出':
			return render_template('index.html',name=request.values['user'])
	return render_template('index.html',name="")

def connect():
	connect = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='109ab0716',
                     database='baseball')

	cursor = connect.cursor()
	cursor.execute("SELECT VERSION()")
	data = cursor.fetchone()
	print ("Database version : %s " % data)
	db.close()