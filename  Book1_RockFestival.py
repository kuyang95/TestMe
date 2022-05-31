N = int(input())

for i in range(0, N):
    L = int(input().split(" ")[1])
    expense = list(map(int,input().split(" ")))
    minEx = [300.0, 0]
    temp = 0
    
    for j in range(0, len(expense)-L+1):
        for k in range(0, L):
            temp += expense[j+k]
        
        if temp < minEx[0]:
            minEx[0] = temp
            minEx[1] = j

        temp = 0
    
    minEx[0] = minEx[0] / L 

    for j in range(minEx[1]+L, len(expense)+1):
        if minEx[0] >= expense[j]:
            print(expense[j])
            minEx[0] = (minEx[0]*L + expense[j])/(L+1)
            L += 1
        
        else:
            break

    for j in range(minEx[1]-1,-1):
        if minEx[0] >= expense[j]:
            minEx[0] = (minEx[0]*L + expense[j])/(L+1)
            L += 1
        
        else:
            break
    
    print(minEx[0])
   
