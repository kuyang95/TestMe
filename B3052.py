A= []

c=0
for i in range(10):
    num = int(input())%42
    A.append(num)
    if A.count(num)==1:
        c+=1
print(c)
