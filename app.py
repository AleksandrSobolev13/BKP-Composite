# 
#!/usr/bin/env python3
import numpy as np
import pandas as pd
import flask
import pickle4 as pickle
from flask import Flask
from flask import request
from flask import render_template
# from tensorflow import keras
from joblib import Memory

# app = flask.Flask(__name__, template_folder = 'templates') 
app = Flask(__name__, template_folder = 'templates')

loaded_model = pickle.load(open('model_predict2.pkl', 'rb', protocol=5))

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])


# loaded_scaler_y = pickle.load(open('model_scaler_y.pkl', 'rb'))


# @app.route('/', methods = ['POST', 'GET'])
# @app.route('/index', methods = ['POST', 'GET'])
return render_template('index.html', result = 5)


#def main():
	#if request.method == 'GET':
		#return render_template('index.html') 
	#if request.method == 'POST':
		# exp1 = request.form.get('experience1')
		# params.append(exp1)
		#return  render_template('index.html', result = 5)
		
	# request.form.get('username'), request.form.get('password')):
	# request.form['username'])
	# params = []
        # alarm_form = []
	      	
	# return  render_template('index.html', result = exp1)

if __name__ == '__main__':
	app.run()


