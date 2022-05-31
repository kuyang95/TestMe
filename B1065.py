def solve(X):
    count = 0
    for i in range(1,int(X)+1):
        if i < 100:
            count += 1
        elif i <1000:
            if int(list(str(i))[0]) - int(list(str(i))[1]) == int(list(str(i))[1]) - int(list(str(i))[2]):
                count += 1
    print(count)

X = input()
solve(X)


        