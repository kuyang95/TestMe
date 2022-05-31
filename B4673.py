def solve(numbers, a):
    a = a + sum(list(map(int,str(a))))
    numbers[a-1] = ''

numbers = list(range(1,11000))
for i in range(1,10000):
    solve(numbers,i)

numbers[10002:] = ''
numbers = list(filter(("").__ne__,numbers))
for j in numbers:
    print(j)


