import sys

def solve(a):
    return sum(a)
    
a = []
lines = sys.stdin.readlines()
for line in lines:
    a.append(int(line))

    print(solve(a))

