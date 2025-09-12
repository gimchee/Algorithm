# 2025-09-12
# SWEA 9367 점점 커지는 당근의 개수



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    C = list(map(int, input().split()))

    count = 1
    max_count = 1

    for i in range(N-1):
        if C[i] < C[i+1]:
            count += 1
        else:
            count = 1

        max_count = max(max_count,count)

    print(f'#{tc} {max_count}')        

