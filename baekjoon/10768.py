a= 2
b = 18

m = int(input())
d = int(input())

if m>a or (m == a and d>b):
    print("After")
elif (m == a and d<b) or m<a:
    print("Before")
elif m==a and b==d:
    print("Special")