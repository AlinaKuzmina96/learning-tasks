"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
"""

import requests

#a = [994, 931, 963, 999, 935, 905, 969, 946, 979, 947, 914, 915, 957, 990, 927]
a = map(int, input().split(","))
params = {
        'json': 'true'
}
for i in a:
    api_url = "http://numbersapi.com/"+str(i)+"/math"
    res = requests.get(api_url, params=params)
    data = res.json()
    if data['found'] == True:
        print("Interesting")
    else:
        print("Boring")
