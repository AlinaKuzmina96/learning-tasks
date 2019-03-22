"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите
их имена в лексикографическом порядке.
"""

import requests, json

client_id = '95c8d957f00037307fc0'
client_secret = 'b6bd335be2bb2b436e942225a0de27cf'
api_url = "https://api.artsy.net/api/tokens/xapp_token"
r = requests.post(api_url,
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token": token}
d = {}
with open("dataset_24476_4.txt") as fi:
   for line in fi:
       a = "https://api.artsy.net/api/artists/" + str(line.rstrip())
       r = requests.get(a, headers=headers)
       j = json.loads(r.text)
       d.update({j['birthday']: j['sortable_name']})

for k in sorted(d.keys()):
    print(d[k])