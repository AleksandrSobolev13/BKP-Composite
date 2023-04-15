# Создаем пользовательское приложение для прогнозирования "соотношения матрица-наполнитель"
# Импортируем необходимые библиотеки для нашего приложения
#import numpy as np
#import tensorflow as tf
import pandas as pd
from tensorflow import keras
from flask import Flask, request, render_template
import flask
from flask import render_template
from flask import request
import pickle
import sklearn
from  sklearn.linear_model import LinearRegression


app = flask.Flask(__name__, template_folder = 'templates')  
# И создаём папку templates in VSCode
# Создаём декораторы для работы с HTML страницами и методы POST GET
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html') 
        # Сразу создать в папке templates in VSCode файлик main.html
    if flask.request.method == 'POST':
        #with open('/home/alexander/Документы/BKP_A_Sobolev/model.pkl', 'rb') as f:
            #loaded_model = pickle.load(f)
        X_test_load = pd.read_excel(r"/home/alexander/Документы/BKP_A_Sobolev/X_test2-0rows.xlsx")
        X_test_ready = pd.DataFrame(X_test_load)
        params = []
        exp1 = float(flask.request.form['experience1'])
        params.append(exp1)
        exp2 = float(flask.request.form['experience2'])
        params.append(exp2)
        exp3 = float(flask.request.form['experience3'])
        params.append(exp3)
        exp4 = float(flask.request.form['experience4'])
        params.append(exp4)
        exp5 = float(flask.request.form['experience5'])
        params.append(exp5)
        exp6 = float(flask.request.form['experience6'])
        params.append(exp6)
        exp7 = float(flask.request.form['experience7'])
        params.append(exp7)
        exp8 = float(flask.request.form['experience8'])
        params.append(exp8)
        exp9 = float(flask.request.form['experience9'])
        params.append(exp9)
        exp10 = float(flask.request.form['experience10'])
        params.append(exp10)
        exp11 = float(flask.request.form['experience11'])
        params.append(exp11)
        exp12 = float(flask.request.form['experience12'])
        params.append(exp12)
        data_from = {'Плотность, кг/м3' : [exp1], 'модуль упругости, ГПа' : [exp2], 'Отвердитель, %' : [exp3],'Эпокс. группы, %' : [exp4], 'Температура вспышки, С_2' : [exp5],'Поверхностная плотность, г/м2' : [exp6], 'Модуль упругости при растяжении, ГПа' : [exp7], 'Прочность при растяжении, МПа' : [exp8], 'Потребление смолы, г/м2' : [exp9], 'Угол нашивки, град' : [exp10], 'Шаг нашивки' : [exp11], 'Плотность нашивки' : [exp12]}
        experie = pd.DataFrame.from_dict(data_from)
        print('\n')
        print(data_from)
        print('\n')
        print(experie)
        print('\n')
        print(params)

        #prediction = loaded_model.predict([exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11, exp12])
        #data_from = {'Плотность, кг/м3' : exp1, 'модуль упругости, ГПа' : exp2, 'Отвердитель, %' : exp3,'Эпокс. группы, %' : exp4, 'Температура вспышки, С_2' : exp5,'Поверхностная плотность, г/м2' : exp6, 'Модуль упругости при растяжении, ГПа' : exp7, 'Прочность при растяжении, МПа' : exp8, 'Потребление смолы, г/м2' : exp9, 'Угол нашивки, град' : exp10, 'Шаг нашивки' : exp11, 'Плотность нашивки' : exp12}
        #exp = pd.DataFrame.from_dict(data_from)
        #y_pred = loaded_model.predict([[params]])
        return  render_template('main.html', result = exp1+exp2+exp3)
#for 2D array  y_pred :[ [  ] ]
    
if __name__ == '__main__':
	app.run()


