himdulda = []
for i in range(10):
    jagoshipda = int(input())
    if jagoshipda%42 not in himdulda:
        himdulda.append(jagoshipda%42)
print(len(himdulda))