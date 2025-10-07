# 2025-10-17
# 백준 2439 별찍기-2


N = int(input())
space = " "
start = "*"

for i in range(1, N+1):
    print(space*(N-i) + start*i)
