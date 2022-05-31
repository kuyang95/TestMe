T = input()
answer = 0

for c in range(int(T)):
    score = input().split("X")
    for i in score:
        temp=i.count("O")
        answer+=int(temp*(temp+1)/2)
    print(answer)   
    answer=0

