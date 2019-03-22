"""Нарисуйте гистограмму распределения веса, роста.
Добавить третий признак - индекс массы тела.
Постройте картинку, на которой будут отображены попарные зависимости признаков , 
'Height', 'Weight' и 'BMI' друг от друга.
Создайте новый признак weight_category, который будет иметь 3 значения: 1 – если вес 
меньше 120 фунтов. (~ 54 кг.), 3 - если вес больше или равен 150 фунтов (~68 кг.), 
2 – в остальных случаях. Постройте «ящик с усами» (boxplot), демонстрирующий 
зависимость роста от весовой категории. 
Постройте scatter plot зависимости роста от веса.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import scipy.optimize as scp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = pd.read_csv('weights_heights.csv', index_col='Index')
data.plot(y='Height', kind='hist', 
           color='red',  title='Height (inch.) distribution')
plt.show()
data.plot(y='Weight', kind='hist', 
           color='green',  title='Weight (inch.) distribution')
plt.show()

def make_bmi(height_inch, weight_pound):   #индекс массы тела
    METER_TO_INCH, K
    +ILO_TO_POUND = 39.37, 2.20462
    return (weight_pound / KILO_TO_POUND) / \
           (height_inch / METER_TO_INCH) ** 2

data['BMI'] = data.apply(lambda row: make_bmi(row['Height'], 
                                              row['Weight']), axis=1)
sns.pairplot(data)
plt.show()

def weight_category(weight):
    if weight < 120:
    	return 1
    elif weight >= 150:
    	return 3
    else:
    	return 2

data['weight_cat'] = data['Weight'].apply(weight_category)
sns.boxplot(x="weight_cat", y="Height", data=data)
plt.show()
data.plot(y='Height', x='Weight', kind='scatter')
plt.show()

def error(w1, w0, data):
    summa = 0.0
    for _, row in data.iterrows():
        summa += (row['Height'] - (w0 + w1 * row['Weight']))**2
    return summa

x = np.linspace(50, 200)
data.plot(y='Height', x='Weight', kind='scatter')
plt.plot(x, 60 + 0.05 * x, color='red')
plt.plot(x, 50 + 0.16 * x, color='green')
plt.legend( ('line (60, 0.05)', 'line (50, 0.16)') )
w1 = np.arange(-5.0, 5.0, 0.25)
plt.plot(w1, error(w1, 50, data))
plt.show()

w1_opt = scp.minimize_scalar(error, bounds=(-5, 5), args=(50, data))

plt.plot(x, 50 + w1_opt.x * x)
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d') # get current axis
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = error(Y, X, data)
surf = ax.plot_surface(X, Y, Z)
ax.set_xlabel('Intercept')
ax.set_ylabel('Slope')
ax.set_zlabel('Error')
plt.show()

def yy(w):
    return error(w[1], w[0], data)

w_opt = scp.minimize(yy, [0.0, 0.0], method='L-BFGS-B', bounds=([-100, 100], [-5, 5]))
#print(w_opt)

plt.plot(x, w_opt.x[0] + w_opt.x[1] * x, color='red')
plt.show()