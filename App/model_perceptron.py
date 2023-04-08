import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor

result_clean = pd.read_excel(r"/home/alexander/Документы/BKP/result_clean.xlsx")

scaler = MinMaxScaler()
result_norm = pd.DataFrame(scaler.fit_transform(result_clean), index=result_clean.index, columns=result_clean.columns)

y2 = result_norm["Пропорции, %"]
x2 = result_norm.drop(columns = ["Пропорции, %"])
X_train2, X_test2, Y_train2, Y_test2 = train_test_split(x2, y2, test_size = 0.3, random_state = 64)

mlp2 = MLPRegressor(random_state = 1, max_iter = 500)
mlp2.fit(X_train2, Y_train2)
Y_pred_mlp2 = mlp2.predict(X_test2)
print('Y predict =', Y_pred_mlp2)
print


# Сохранение модели
pickle.dump(mlp2, open('model_perceptron.pkl', 'wb'))





