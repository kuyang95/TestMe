T = input()
c=0
for i in range(int(T)):
    N = list(map(int,input().split()))
    avg = (sum(N) - N[0])/N[0]
    for a in N[1:]:
        if a>avg:
            c+=1
    print("{0:.3f}".format(c/N[0]*100)+ "%")
    c=0
    