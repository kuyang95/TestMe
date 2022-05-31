A=int(input())
B=int(input())
C=int(input())
N=A*B*C
for i in range(0,10):
    print(str(N).count(str(i)))
