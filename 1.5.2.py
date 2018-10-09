"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой
последовательности, затем сумму второй пятерки, и т. д.
Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. Например,
сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных
элементов по мере их накопления.
Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо,
т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
Обратите внимание, что во время выполнения метода add выводить сумму пятерок может потребоваться несколько раз до тех пор,
пока в буфере не останется менее пяти элементов.
"""

class Buffer:
    def __init__(self):
        self.lst = []
        self.list = []

    def add(self, *a):
        for j in a:
            self.lst.append(j)
        l = len(self.lst)
        s = 0
        while l > 4:
            if l == 5:
                for i in range(5):
                    s = s + self.lst[i]
                print(s)
                self.lst = []
                l = len(self.lst)
            else:
                for i in range(0, 5):
                    s = s + self.lst[i]
                print(s)
                s = 0
                for i in range(5, l):
                    self.list.append(self.lst[i])
                self.lst = self.list
                self.list = []
                l = len(self.lst)

    def get_current_part(self):
        return self.lst

"""
class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part
"""