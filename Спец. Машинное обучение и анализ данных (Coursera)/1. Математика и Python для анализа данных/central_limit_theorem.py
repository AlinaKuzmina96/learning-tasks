"""Для выполнения задания была выбрана функция распределения Парето. Были построены для четырех 
разных n (5, 30, 100, 1000) по 1000 случайных выборок, измерены их выборочные средние и 
составлены соостветствующие массивы, по массивам выборочных средних построены гистограммы 
распределения, исходя из теоретических данных определены соответствующие каждому n параметры 
распределений для аппроксимации, по полученным параметрам построены функции нормального 
распределения для каждого n поверх соответствующих гистограмм.

По полученным графикам наблюдается увелечение точности апроксимации выборочного среднего 
значения непрерывной случайной величины описываемой распределением Парето. Заметна 
скошенность проявляющаяся в несимметричности распределения относительно центра. Функция 
сходится медленно, и более качественный результат наблюдается при больших n, в нашем случае 
при n = 1000."""

import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
import math

pareto = st.pareto(3) #распределение Парето
viborka = pareto.rvs(size=1000) #выборка
x = np.linspace(0, 10, 1000)
pdf = pareto.pdf(x) #функция плотности распределения

plt.plot(x, pdf, label='theoretical PDF')
plt.hist(viborka, bins =50, range=(1,10), normed=True)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
plt.show()

#посчитаем среднее и дисперсию
xm=1.#минимальное значение
k=3.# k -> это параметр b - "коэффициент кривизны"
E=(xm*k)/(k-1)#среднее(мат ожидание)
D=(E**2)*(k/(k-2))#дисперсия

n=5
sample5=np.array([])#обозначим массив выборочных средних
i=1
while i <= 1000:#цикл генерации случайных выборок количества n из функции
    sample5i = pareto.rvs(n)#генерация выборки
    mean5i=sum(sample5i)/n#определение выборочного среднего (в.с.)
    sample5=np.append(sample5,mean5i)#добавляем в массив новое значение в.с.
    i+=1
#определим параметры нормального распределения описывающие массив 1000 в.с. при n=5
D5=D/n#дисперсия для нормального распределения приближающего выборку средних
sigma5=math.sqrt(D5)#сигма для нормального распределения выборки средних
norm5 = st.norm(E, sigma5)#определяем нормальное распределение с расчетными характеристиками Парето
pdf5 = norm5.pdf(x[:500])#получаем плотность распределения
#строим гистограмму массива средних при n=5 и плотность описывающую этот массив нормального распределения
plt.plot(x[:500], pdf5, label='PDF(n=5)')
plt.hist(sample5, bins =80, range=(0,5), normed=True)
plt.ylabel('number of samples')
plt.xlabel('$x$')
plt.show()

n=30
sample30=np.array([])
i=1
while i <= 1000:
    sample30i = pareto.rvs(n)
    mean30i=sum(sample30i)/n
    sample30=np.append(sample30,mean30i)
    i+=1
D30=D/n
sigma30=math.sqrt(D30)
norm30 = st.norm(E, sigma30)
pdf30 = norm30.pdf(x[:300])
plt.plot(x[:300], pdf30, label='PDF(n=30)')
plt.hist(sample30, bins =80, range=(0,3), normed=True)
plt.ylabel('number of samples')
plt.xlabel('$x$')
plt.show()

n=100
sample100=np.array([])
i=1
while i <= 1000:
    sample100i = pareto.rvs(n)
    mean100i=sum(sample100i)/n
    sample100=np.append(sample100,mean100i)
    i+=1
D100=D/n
sigma100=math.sqrt(D100)
norm100 = st.norm(E, sigma100)
pdf100 = norm100.pdf(x[:300])
plt.plot(x[:300], pdf100, label='PDF(n=100)')
plt.hist(sample100, bins =80, range=(0,3), normed=True)
plt.ylabel('number of samples')
plt.xlabel('$x$')
plt.show()

n=1000
sample1000=np.array([])
i=1
while i <= 1000:
    sample1000i = pareto.rvs(n)
    mean1000i=sum(sample1000i)/n
    sample1000=np.append(sample1000,mean1000i)
    i+=1
D1000=D/n
sigma1000=math.sqrt(D1000)
norm1000 = st.norm(E, sigma1000)
pdf1000 = norm1000.pdf(x[:300])
plt.plot(x[:300], pdf1000, label='PDF(n=1000)')
plt.hist(sample1000, bins =80, range=(0,3), normed=True)
plt.ylabel('number of samples')
plt.xlabel('$x$')
plt.show()
