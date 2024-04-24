a,b,c = map(int,input().split())
r = a/(b**2+c**2)**0.5
# b의 제곱과 c의 제곱을 더하고 거기에 0.5의 제곱을 곱한 뒤 a로 나눈다.
print(int(b*r),int(c*r))