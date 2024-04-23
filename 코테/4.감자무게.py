n = int(input())
num = 0
for i in range(n):
    k = int(input())
    num += k
    s = num/1000
if 4.7<=s<=5:
    print("당신은 인간 저울이군.")
elif s<4.7 or s>5:
    print("이 감자 네가 다 먹고 다시 가져와.")
elif s == 0:
    print("장난해?")
