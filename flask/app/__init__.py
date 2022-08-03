from flask import Flask
from flask_cors import CORS
from app.route import index

def create_app(): 
	app = Flask(__name__,template_folder='templates')
	CORS(app)
	app.add_url_rule('/', '/', index, methods=['POST','GET'])
	return app


