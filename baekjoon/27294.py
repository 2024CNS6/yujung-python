t,s = map(int,input().split())
if t<=11:
    print("280")
elif 12<=t<=16 and s == 1:
    print("280")
elif 12<=t<=16:
    print("320")
else:
    print("280")