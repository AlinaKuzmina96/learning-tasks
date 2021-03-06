"""Напишите дескриптор Value, который будет использоваться в нашем классе Account.
У аккаунта будет атрибут commission. Именно эту коммиссию и нужно вычитать при 
присваивании значений в amount."""

class Value:
    def __init__(self):
        self.value = None
    
    @staticmethod
    def _prepare_value(value, obj):
        return value - (value * obj.commission)

    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.value = self._prepare_value(value, obj)

class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)