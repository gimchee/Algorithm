# 2025-09=28
# SWEA 1959 두 개의 숫자열.



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) < len(B):
        A,B = B,A
    
    max_sum = -23333
    for i in range(len(A)-len(B)+1):
        temp = 0 
        for j in range(len(B)):
            temp += (A[j+i] * B[j])
        if max_sum < temp:
            max_sum = temp

    print(f'#{tc} {max_sum}')
