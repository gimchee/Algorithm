# 2025-09-10
# SWEA 9386 연속한 1의 개수


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    num = input()

    count = 0
    max_count = 0

    for i in range(N):

        # 1인경우, count 증가
        # max_count에 최대값 누적 업데이트
        if num[i] == '1':
            count += 1
            max_count = max(max_count, count)
        # 1이 아닌겨우, 초기화
        else:
            count = 0
    
    print(f'#{tc} {max_count}')