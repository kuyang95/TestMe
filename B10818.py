N = []
for i in range(9):
    N.append(int(input()))
print(max(N),"\n",N.index(max(N))+1,sep="")