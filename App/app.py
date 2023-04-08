import flask
from flask import render_template
from flask import request
import pickle
import pandas as pd 		
import numpy as np 		

app = flask.Flask(__name__, template_folder = 'templates') 

# Создаём декораторы, которые будут работать с нашими страницами и методы POST GET
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])

def main():
	param_lst = []
	if flask.request.method == 'GET':
		return render_template('main.html') 
	# Сразу создаём main.html в папке templates
	
	if flask.request.method == 'POST':
		with open('/home/alexander/Документы/BKP_A_Sobolev/model_perceptron.pkl', 'rb') as f:
			loaded_model = pickle.load(f)
		
		exp1 = float(flask.request.form.get['experience1'])
		param_lst.append(float(exp1))
		
		exp2 = float(flask.request.form.get['experience2'])
		param_lst.append(float(exp2))
		
		exp3 = float(flask.request.form.get['experience3'])
		param_lst.append(float(exp3))
		
		exp4 = float(flask.request.form.get['experience4'])
		param_lst.append(float(exp4))
		
		exp5 = float(flask.request.form.get['experience5'])
		param_lst.append(float(exp5))
		
		exp6 = float(flask.request.form.get['experience6'])
		param_lst.append(float(exp6))
		
		exp7 = float(flask.request.form.get['experience7'])
		param_lst.append(float(exp7))
		
		exp8 = float(flask.request.form.get['experience8'])
		param_lst.append(float(exp8))
		
		exp9 = float(flask.request.form.get['experience9'])
		param_lst.append(float(exp9))
		
		exp10 = float(flask.request.form.get['experience10'])
		param_lst.append(float(exp10))
		
		exp11 = float(flask.request.form.get['experience11'])
		param_lst.append(float(exp11))
		
		exp12 = float(flask.request.form.get['experience12'])
		param_lst.append(float(exp12))
		
		print('param_lst =', param_lst)
		

		data_from = {'Плотность, кг/м3' : exp1, 'модуль упругости, ГПа' : exp2, 'Отвердитель, %' : exp3,'Эпокс. группы, %' : exp4, 'Температура вспышки, С_2' : exp5,'Поверхностная плотность, г/м2' : exp6, 'Модуль упругости при растяжении, ГПа' : exp7, 'Прочность при растяжении, МПа' : exp8, 'Потребление смолы, г/м2' : exp9, 'Угол нашивки, град' : exp10, 'Шаг нашивки' : exp11, 'Плотность нашивки' : exp12}
		exp = pd.DataFrame.from_dict(data_from)

		print('point stop', len(exp))

 
		y_pred = loaded_model.predict([[exp]]) 
		#y_pred = loaded_model.predict([[param_lst]])
		return  render_template('main.html', result = exp2, )
	
if __name__ == '__main__':
	app.run()
#X = np.array(experience).reshape(-1, 1)  # reshape для исключения конфликта размерности массивов
#y = np.array(salary)
# Сразу сохранить в папке ML_Flask в VSCode файлик app.py
# и  переходим к написанию main.html




