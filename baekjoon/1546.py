subject_num = int(input())
score = list(map(int,input().split()))
M = max(score)
for i in range(subject_num):
    score[i]= score[i]/M*100

print(sum(score)/subject_num)