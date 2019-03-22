"""Рассмотрим функцию: f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2), на промежутке [1, 30].
   В первом задании будем искать минимум этой функции на заданном промежутке с помощью 
scipy.optimize. Напишите на Питоне функцию, вычисляющую значение f(x) по известному x. 
Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize 
(т.е. задав только функцию и начальное приближение). Mетод BFGS.
Теперь измените начальное приближение на x=30. 
    Теперь попробуем применить к той же функции f(x) метод глобальной оптимизации — 
дифференциальную эволюцию. Запустите поиск минимума функции f(x) с помощью дифференциальной 
эволюции на промежутке [1, 30].
    Теперь рассмотрим функцию h(x) = int(f(x)) на том же отрезке [1, 30]. Попробуйте найти 
минимум функции h(x) с помощью BFGS, взяв в качестве начального приближения x=30. 
Теперь попробуйте найти минимум h(x) на отрезке [1, 30] с помощью дифференциальной эволюции. 
"""
   

import math
import scipy.optimize

def f(x, *args):
	return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

print(scipy.optimize.minimize(f, 2))                           #1 
print(scipy.optimize.minimize(f, 2, method='BFGS'))            #1
print(scipy.optimize.minimize(f, 30, method='BFGS'))           #1

print(scipy.optimize.differential_evolution(f, [(1, 30)]))     #2

def h(x, *args):
	return int(math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2))

print(scipy.optimize.minimize(h, 30, method='BFGS'))           #3
print(scipy.optimize.differential_evolution(h, [(1, 30)]))     #3
