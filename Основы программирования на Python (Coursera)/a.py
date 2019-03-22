dic = {}
text = ''
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        if line[0] == 'BALANCE':
            if line[1] in dic:
                text = text + str(dic[line[1]]) + '\n'
            else:
                text = text + 'ERROR' + '\n'
        else:
            if line[1] not in dic:
                dic[line[1]] = 0
            if line[0] == 'DEPOSIT':
                dic[line[1]] += int(line[2])
            elif line[0] == 'WITHDRAW':
                dic[line[1]] -= int(line[2])
            elif line[0] == 'TRANSFER':
                if line[2] not in dic:
                    dic[line[2]] = 0
                dic[line[1]] -= int(line[3])
                dic[line[2]] += int(line[3])
            elif line[0] == 'INCOME':
                for key in dic:
                    a = dic[key]
                    if a > 0:
                        dic[key] = int(a + a * (int(line[1])/100))

with open('output.txt', 'w', encoding='utf-8') as g:
    g.write(text)
