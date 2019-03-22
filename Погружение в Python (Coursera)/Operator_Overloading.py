"""Создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных 
операций.
Класс инициализируется полным путем.
Класс должен поддерживать метод write.
Объекты типа File должны поддерживать сложение.
В этом случае создается новый файл и файловый объект, в котором содержимое второго файла 
добавляется к содержимому первого файла. Новый файл должен создаваться в этой же директории. 
Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам 
файла.
При выводе файла с помощью функции print должен печататься его полный путь, переданный при 
инициализации.
"""

class File():
	def __init__(self, path, mode='r+'):
		self.path = path
		self.mode = mode
		self.counter = 0

	def text(self):
		with open(self.path, self.mode) as f:
			t = ''
			for i in f:
				t += i
		return t

	def write(self, text):
		with open(self.path, self.mode) as f:
			f.write(text)

	def __add__(self, other):
		a = self.text()
		b = other.text()
		new_obj_text = a + b
		new_obj = File('text1+text2.txt', 'w').write(new_obj_text)
		return File('text1+text2.txt')

	def __next__(self):
		t = self.text().split('\n')
		if self.counter < len(t):
			self.counter += 1
			return t[self.counter - 1]
		else:
			raise StopIteration

	def __str__(self):                                             
		return self.path



first = File('text1.txt')
second = File('text2.txt')
new_obj = first + second
print(next(new_obj))
print(next(new_obj))
print(next(new_obj))
print(next(new_obj))
