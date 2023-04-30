# Создаем пользовательское приложение для прогнозирования "соотношения матрица-наполнитель"

import numpy as np
import pandas as pd
import flask
from tensorflow import keras
from flask import Flask, request, render_template
from joblib import load
# import pickle
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.neural_network import MLPRegressor



app = flask.Flask(__name__, template_folder = 'templates')  

loaded_scaler_x = load('https://github.com/AleksandrSobolev13/BKP-Composite/blob/main/model_scaler_x.joblib')
loaded_scaler_y = load('https://github.com/AleksandrSobolev13/BKP-Composite/blob/main/model_scaler_y.joblib')
loaded_model = load('https://github.com/AleksandrSobolev13/BKP-Composite/blob/main/model_predict2.joblib')

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html') 
    if flask.request.method == 'POST':
        params = []
        alarm_form = []

        exp1 = float(flask.request.form['experience1'])
        params.append(exp1)
        if (exp1 < 1790 or exp1 > 2160):
            alarm_form.append('Плотностb, кг/м3')

        exp2 = float(flask.request.form['experience2'])
        params.append(exp2)
        if (exp2 < 3 or exp2 > 1600):
            alarm_form.append('Модуля упругости, ГПа')

        exp3 = float(flask.request.form['experience3'])
        params.append(exp3)
        if (exp3 < 40 or exp3 > 180):
            alarm_form.append('% Отвердителя')

        exp4 = float(flask.request.form['experience4'])
        params.append(exp4)
        if (exp4 < 16 or exp4 > 27):
            alarm_form.append('% Эпокс. группы')

        exp5 = float(flask.request.form['experience5'])
        params.append(exp5)
        if (exp5 < 180 or exp5 > 385):
            alarm_form.append('Температура вспышки')

        exp6 = float(flask.request.form['experience6'])
        params.append(exp6)
        if (exp6 < 2 or exp6 > 1290):
            alarm_form.append('Поверхностная плотность, г/м2')

        exp7 = float(flask.request.form['experience7'])
        params.append(exp7)
        if (exp7 < 67 or exp7 > 80):
            alarm_form.append('Модуль упругости при растяжении')

        exp8 = float(flask.request.form['experience8'])
        params.append(exp8)
        if (exp8 < 1250 or exp8 > 3700):
            alarm_form.append('Прочность при растяжении, МПа')

        exp9 = float(flask.request.form['experience9'])
        params.append(exp9)
        if (exp9 < 64 or exp9 > 350):
            alarm_form.append('Потребление смолы, г/м2')

        exp10 = float(flask.request.form['experience10'])
        params.append(exp10)
        if (exp10 != 0.0 and exp10 != 1.0):
            alarm_form.append('Угол нашивки, град')

        exp11 = float(flask.request.form['experience11'])
        params.append(exp11)
        if (exp11 < 1 or exp11 > 13):
            alarm_form.append('Шаг нашивки')

        exp12 = float(flask.request.form['experience12'])
        params.append(exp12)
        if (exp12 < 28 or exp12 > 85):
            alarm_form.append('Плотность нашивки')

        data_from = {'Плотность, кг/м3' : [exp1], 'модуль упругости, ГПа' : [exp2], 'Отвердитель, %' : [exp3],'Эпокс. группы, %' : [exp4], 'Температура вспышки, С_2' : [exp5],'Поверхностная плотность, г/м2' : [exp6], 'Модуль упругости при растяжении, ГПа' : [exp7], 'Прочность при растяжении, МПа' : [exp8], 'Потребление смолы, г/м2' : [exp9], 'Угол нашивки, град' : [exp10], 'Шаг нашивки' : [exp11], 'Плотность нашивки' : [exp12]}
        experie = pd.DataFrame.from_dict(data_from)
        
        print('\n')
        print('Из  web формы возвращены 12 значений в виде словаря:', params)
        print('\n')
        # print('Словарь из web формы преобразован в pd.DataFrame:')
        # print(experie.T)
        # for i in experie:
        #       experie = [float(i.replace(',', '.'))]
        
        x4 = loaded_scaler_x.transform(experie)
        x3 = pd.DataFrame(x4, index=experie.index, columns=experie.columns)
        
        #print('\n')
        # print('pd.DataFrame после обработки loaded_scaler_x:')
        # print(x3.T)
        # print('\n')
        y_pred = loaded_model.predict(x3) 
        # print('\n')
        # print('Предсказанное значение Y до inverse_transform = ', y_pred.T)
        # print('\n')   
        y_nature = loaded_scaler_y.inverse_transform(y_pred.reshape(-1,1))
        print('Значение Y после inverse_transform отправляем в web = ', y_nature.T)
        print('angle = ', exp10)
        print('\n')
        if not alarm_form:
            return  render_template('main.html', result = y_nature, data = data_from)
        return  render_template('main.html', result = y_nature, data = data_from, alarm_to = alarm_form )
#for 2D array  y_pred :[ [  ] ] 
if __name__ == '__main__':
    app.run()



