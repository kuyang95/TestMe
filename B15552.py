import sys

T = sys.stdin.readline().rstrip()

for i in range(int(T)):
    N = list(map(int,sys.stdin.readline().rstrip().split()))
    print(N[0]+N[1])