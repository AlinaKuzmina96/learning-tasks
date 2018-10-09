"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания
пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
Вашей программе на вход подаются следующие запросы:
    create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства
    <namespace>, или None, если такого пространства не существует
Более формально, результатом работы get <namespace> <var> являетсz
    <namespace>, если в пространстве <namespace> была объявлена переменная <var>
    get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
    None, если не существует <parent>, т. е. <namespace>﻿ – это global
"""

d = {'global': {'parent': 'None', 'vars': []}}

def get(nms, var):
	if nms == 'None':
		return 'None'
	elif str(var) in d[str(nms)]['vars']:
		return nms
	else:
		return get(d[str(nms)]['parent'], str(var))

n = int(input())
for i in range(n):
	q, w, e = input().split()
	if q == 'create':
		d.update({w: {'parent': e, 'vars': []}})
	elif q == 'add':
		d[w]['vars'].append(e)
	elif q == 'get':print(get(w, e))