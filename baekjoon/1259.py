# while True:
#     n = list(map(int, input().strip()))
#     m = []
#     if n == 0:
#         break
 
#     for i in range(len(n), 0, -1):
#         m.append(n[i-1])
#     for j in range(len(n), 0, -1) :
#         if m[i-1] == n[i-1] :
#             continue
#         else :
#             break
    
    #     m.append(n[i])
    # print(m)
    

while True:
    n = input()

    if n=='0':
        break
    if n==n[::-1]:
        print('yes')
    else:
        print('no')