# 2025-09-12
# SWEA 11092

'''
최대 최소의 간격

최대값의 위치, 최소값의 위치 차이 절대값 출력
작은 수 여러개 : 가장 먼저 나오는 위치
큰 수 여러개 : 가장 마지막 나오는 위치

'''


T = int(input())

for tc in range(1, T+1):

    # 정수의 개수
    N = int(input())
    # 정수
    ai = list(map(int, input().split()))

    min_val = 10000
    max_val = 0

    min_idx = 0
    max_idx = 0


     # 일단 최소값, 최대값 찾기 반복문

    for i in range(N):
        
        if min_val > ai[i]:
            min_val = ai[i]

        if max_val < ai[i]:
            max_val = ai[i]

     # 왼쪽 -> 오른쪽 최소값이면 탈출. 인덱스 찾기

    for j in range(N):
        if ai[j] == min_val:
            min_idx = j
            break

     # 오른쪽 -> 왼쪽 최대 값이 탈출, 인덱스 찾기
    for k in range(N-1,-1,-1):
        if ai[k] == max_val:
            max_idx = k
            break    

    # 차이의 절대값 출력하기

    if(min_idx - max_idx) > 0:
        print(f'#{tc} {min_idx-max_idx}')
    else:
        print(f'#{tc} {max_idx - min_idx}')
