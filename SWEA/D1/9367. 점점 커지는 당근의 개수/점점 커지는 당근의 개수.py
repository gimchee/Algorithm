# 2025-09-06 
# SWEA 9367. 점점 커지는 당근의 개수



T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    C = list(map(int, input().split()))

    count = 1
    temp = 0
    max_count = 1
    for i in range(1,N):

        if C[i-1] < C[i]:

            count += 1
   
        else:

            count = 1

        max_count = max(count, max_count)
    print(f'#{test_case} {max_count}')