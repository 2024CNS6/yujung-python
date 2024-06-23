n = list(map(int,input().split()))
num = n.count(1)

if num == 1:
    print("도")
elif num ==2:
    print("개")
elif num ==3:
    print("걸")
elif num==4:
    print("윷")
else:
    print("모")