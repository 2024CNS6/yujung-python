s = input()
s = s.upper()

s = list(s)

temp = 0
case = ''
res = 0

for i in s:
    temp2 = s.count(i)
    if temp < temp2:
        temp = temp2
        case = i
        res = 0
    elif temp == temp2 and case != i:
        res += 1

if not res:
    print(case)
else:
    print('?')