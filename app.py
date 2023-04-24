# 
import numpy as np
import pandas as pd
import flask
import pickle
from flask import Flask
from flask import request
from flask import render_template


# from tensorflow import keras
# import pickle

app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])


# Создаем пользовательское приложение для прогнозирования "соотношения матрица-наполнитель"
# app = flask.Flask(__name__, template_folder = 'templates') 
# app = Flask(__name__, template_folder = 'templates')
loaded_scaler_x = pickle.load(open('model_scaler_x.pkl', 'rb'))
# loaded_scaler_y = pickle.load(open('model_scaler_y.pkl', 'rb'))
# loaded_model = pickle.load(open('model_predict2.pkl', 'rb'))

# @app.route('/', methods = ['POST', 'GET'])
# @app.route('/index', methods = ['POST', 'GET'])

def main():
	# if request.method == 'GET':
		# return render_template('index1.html') 
	# if request.method == 'POST':
		# exp1 = request.form.get('experience1')
		# params.append(exp1)
		
	# request.form.get('username'), request.form.get('password')):
	# request.form['username'])
	# params = []
        # alarm_form = []
	      	
	return  render_template('index.html', result = exp1)

if __name__ == '__main__':
	app.run()


