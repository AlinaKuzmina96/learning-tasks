"""Предположим есть данные о разных автомобилях и спецтехнике. Данные представлены в виде 
таблицы с характеристиками. Вам необходимо создать свою иерархию классов для данных, которые 
описаны в таблице.
BaseCar
Car(BaseCar)
Truck(BaseCar)
SpecMachine(BaseCar)
У любого объекта есть обязательный атрибут car_type. Он означает тип объекта и может принимать 
одно из значений: car, truck, spec_machine. Также у любого объекта из иерархии есть фото в 
виде имени файла — обязательный атрибут photo_file_name. В базовом классе нужно реализовать 
метод get_photo_file_ext для получения расширения файла (“.png”, “.jpeg” и т.д.) с фото. 
Для грузового автомобиля необходимо разделить характеристики кузова на отдельные составляющие 
body_length, body_width, body_height. Разделитель — латинская буква x. Характеристики кузова 
могут быть заданы в виде пустой строки, в таком случае все составляющие равны 0. 
Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, 
возвращающий объем кузова в метрах кубических.
Далее необходимо реализовать функцию, на вход которой подается имя файла в формате csv. 
Файл содержит данные аналогичные строкам из таблицы. Вам необходимо прочитать этот файл 
построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки и 
создать список нужных объектов с автомобилями и специальной техникой. Функция должна 
возвращать список объектов."""

# -*- coding: utf-8 -*-

import os
import csv
import codecs

class BaseCar():

	def __init__(self, brand, photo_file_name, carrying):
		self.photo_file_name = photo_file_name
		self.brand = brand
		self.carrying = carrying

	def get_photo_file_ext(self):
		ext = os.path.splitext(self.photo_file_name)[1]
		return ext


class Car(BaseCar):

	def  __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):

	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		self.body_whl = body_whl

	def body(self):
		if self.body_whl == '':
			body_length = 0
			body_width = 0
			body_height = 0
		else:
			body_length = float(self.body_whl.split('x')[0])
			body_width = float(self.body_whl.split('x')[1])
			body_height = float(self.body_whl.split('x')[2])
		return [body_length, body_width, body_height]

	def get_body_volume(self):
		v = self.body()[0] * self.body()[1] * self.body()[2]
		return v


class SpecMachine(BaseCar):
	def  __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.extra = extra


def get_car_list(csv_filename):
	with open(csv_filename, encoding='utf-8') as csv_fd:
		reader = csv.reader(csv_fd, delimiter=';')
		next(reader)
		row_list = []  # пропускаем заголовок
		for row in reader:
			row_list.append(row)
	car_list = []
	for i in range(len(row_list)):
		l = row_list[i]
		if len(l) != 0:
			if l[0] == 'car':
				if l[1] != '' and l[2] != '' and l[3] != '' and l[5] != '':
					car_list.append('Car({}, {}, {}, {})'.format(l[1], l[3], float(l[5]), int(l[2])))
			elif l[0] == 'truck':
				if l[1] != '' and l[3] != '' and l[4] != '' and l[5] != '':
					car_list.append('Truck({}, {}, {}, {})'.format(l[1], l[3], float(l[5]), l[4]))
			elif l[0] == 'spec_machine':
				if l[1] != '' and l[6] != '' and l[3] != '' and l[5] != '':
					car_list.append('SpecMachine({}, {}, {}, {})'.format(l[1], l[3], float(l[5]), l[6]))
	return car_list


print(get_car_list('coursera_week3_cars.csv'))



