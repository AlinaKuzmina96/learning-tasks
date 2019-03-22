"""Определить класс FileReader. Инициализатор этого класса принимает аргумент - путь до 
файла на диске.
У класса должен быть метод read, возвращающий содержимое файла в виде строки.
Внутри метода read вы должны обрабатывать исключение IOError, возникающее, когда файла, с 
которым был инициализирован класс, на самом деле нет на жестком диске. В случае 
возникновения такой ошибки метод read должен возвращать пустую строку ""."""

class FileReader():

	def __init__(self, file):
		self.file = file

	def read(self):
		try:
			line = ''
			with open(self.file, "r") as f:
				for lin in f:
					line += lin.strip()
		except IOError:
			line = ''
		return line

reader = FileReader("class_reader_example.txt")
print(reader.read())