a = input("Цепочка 1 ")
b = input("Цепочка 2 ")
List = a.split(' ')
if len(List) > 10000:
    print ("количество цепочек больше 100")
    exit()
list = b.split(' ')
if len(list) > 10000:
    print ("количество цепочек больше 100")
    exit()
for f in List:
    if len(f)>1000:
        print("цепочка в первом языке больше 100")
        exit()
for f in list:
    if len(f)>100:
        print("цепочка во втором языке больше 100")
        exit()
print("Результат")
for i in List:
    for j in list:
        print((i + j) + " ") 