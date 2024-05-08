# s = input()
# s = s.upper()

# s = list(s)

# temp = 0
# case = ''
# res = 0

# for i in s:
#     temp2 = s.count(i)
#     if temp < temp2:
#         temp = temp2
#         case = i
#         res = 0
#     elif temp == temp2 and case != i:
#         res += 1

# if not res:
#     print(case)
# else:
#     print('?')

word = input().upper()
word_list = list(set(word))
lst = []

for i in word_list:
    count = word.count(i)
    lst.append(count)

if lst.count(max(lst))>= 2:
    print("?")
else:
    print(word_list[lst.index(max(lst))])