import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def write_answer_to_file(answer, filename):
    with open(filename, 'w') as f_out:
        f_out.write(str(round(answer, 3)))

adver_data = pd.read_csv('advertising.csv')
print(adver_data[:5])

adver_data.plot(y='TV', kind='hist')
adver_data.plot(y='Radio', kind='hist')
adver_data.plot(y='Newspaper', kind='hist')
adver_data.plot(y='Sales', kind='hist')
plt.show()

#Создайте массивы NumPy X* из столбцов TV, Radio и Newspaper и *y - из столбца Sales. 
X = np.array(adver_data.values[:,0:3])
y = np.array(adver_data.values[:,3])

#Отмасштабируйте столбцы матрицы X, вычтя из каждого значения среднее по 
#соответствующему столбцу и поделив результат на стандартное отклонение.
means, stds = np.mean(X, axis=0), np.std(X, axis=0)
X = (X - means)/stds

#Добавьте к матрице X* столбец из единиц
n = np.shape(X)[0]
ones = np.reshape(np.ones(n),(n,1))
X = np.hstack((X,ones))

#Реализуйте функцию mserror - среднеквадратичную ошибку прогноза.
def mserror(y, y_pred):
    return np.mean((y-y_pred)**2)

#Какова среднеквадратичная ошибка прогноза значений Sales, если всегда предсказывать 
#медианное значение Sales по исходной выборке?
y_med = np.median(y)
answer1 = mserror(y,y_med)
print(answer1)
write_answer_to_file(answer1, '1.txt')

#Реализуйте функцию normal_equation, которая по заданным матрицам (массивам NumPy) X* 
#и *y вычисляет вектор весов 𝑤 согласно нормальному уравнению линейной регрессии.
def normal_equation(X, y):
    w = np.linalg.solve(np.dot(X.transpose(), X), np.dot(X.transpose() ,y))
    return w
norm_eq_weights = normal_equation(X, y)
print(norm_eq_weights)

#Какие продажи предсказываются линейной моделью с весами, найденными с помощью 
#нормального уравнения, в случае средних инвестиций в рекламу по ТВ, радио и в газетах? 
#(то есть при нулевых значениях масштабированных признаков TV, Radio и Newspaper). 
answer2 = np.sum([0, 0, 0, 1]*norm_eq_weights)
print(answer2)
write_answer_to_file(answer2, '2.txt')

#Напишите функцию linear_prediction, которая принимает на вход матрицу X* и вектор 
#весов линейной модели *w, а возвращает вектор прогнозов в виде линейной комбинации 
#столбцов матрицы X* с весами *w.
def linear_prediction(X, w):
	return np.dot(X, w)

#Какова среднеквадратичная ошибка прогноза значений Sales в виде линейной модели с 
#весами, найденными с помощью нормального уравнения? 
lin = linear_prediction(X, norm_eq_weights)
answer3 = mserror(y, lin)
print(answer3)
write_answer_to_file(answer3, '3.txt')

#Напишите функцию stochastic_gradient_step, реализующую шаг стохастического 
#градиентного спуска для линейной регрессии. Функция должна принимать матрицу X*, 
#вектора *y и w*, число *train_ind - индекс объекта обучающей выборки (строки матрицы X*), 
#по которому считается изменение весов, а также число *𝜂(eta) - шаг градиентного спуска 
#(по умолчанию eta=0.01). Результатом будет вектор обновленных весов. 
def stochastic_gradient_step(X, y, w, train_ind, eta=0.01):
    return w + 2 * eta/X.shape[0] * X[train_ind] * (y[train_ind] - linear_prediction(X[train_ind], w))

#Напишите функцию stochastic_gradient_descent, реализующую стохастический градиентный 
#спуск для линейной регрессии. Функция принимает на вход следующие аргументы:
"""
 X - матрица, соответствующая обучающей выборке
 y - вектор значений целевого признака
 w_init - вектор начальных весов модели
 eta - шаг градиентного спуска (по умолчанию 0.01)
 max_iter - максимальное число итераций градиентного спуска (по умолчанию 10000)
 max_weight_dist - максимальное евклидово расстояние между векторами весов на соседних итерациях градиентного спуска, при котором алгоритм прекращает работу (по умолчанию 1e-8)
 seed - число, используемое для воспроизводимости сгенерированных псевдослучайных чисел (по умолчанию 42)
 verbose - флаг печати информации (например, для отладки, по умолчанию False)
На каждой итерации в вектор (список) должно записываться текущее значение 
среднеквадратичной ошибки. Функция должна возвращать вектор весов 𝑤, а также вектор 
(список) ошибок."""
def stochastic_gradient_descent(X, y, w_init, eta=1e-2, max_iter=1e4,
								min_weight_dist=1e-8, seed=42, verbose=False):
# Инициализируем расстояние между векторами весов на соседних
# итерациях большим числом. 
	weight_dist = np.inf
# Инициализируем вектор весов
	w = w_init
# Сюда будем записывать ошибки на каждой итерации
	errors = []
# Счетчик итераций
	iter_num = 0
# Будем порождать псевдослучайные числа 
# (номер объекта, который будет менять веса), а для воспроизводимости
# этой последовательности псевдослучайных чисел используем seed.
	np.random.seed(seed)
# Основной цикл
	while weight_dist > min_weight_dist and iter_num < max_iter:
	# порождаем псевдослучайный 
	# индекс объекта обучающей выборки
		random_ind = np.random.randint(X.shape[0])
		w_new = stochastic_gradient_step(X, y, w, random_ind, eta)
		weight_dist = np.linalg.norm(w-w_new)
		w = w_new
		errors.append(mserror(y, linear_prediction(X, w)))
		iter_num += 1
	return w, errors

#Запустите 10^5 итераций стохастического градиентного спуска. Укажите вектор начальных 
#весов w_init, состоящий из нулей. 
stoch_grad_desc_weights, stoch_errors_by_iter = stochastic_gradient_descent(X, y, np.zeros(X.shape[1]), max_iter=1e5)

#Посмотрим на вектор весов, к которому сошелся метод.
print(stoch_grad_desc_weights)

#Посмотрим на среднеквадратичную ошибку на последней итерации.
print(stoch_errors_by_iter[-1])

#Какова среднеквадратичная ошибка прогноза значений Sales в виде линейной модели с 
#весами, найденными с помощью градиентного спуска? 
answer4 = mserror(y, linear_prediction(X, stoch_grad_desc_weights))
print(answer4)
write_answer_to_file(answer4, '4.txt')