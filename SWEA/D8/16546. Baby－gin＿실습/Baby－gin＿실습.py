T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input().strip()))
    
    counts = [0] * 10
    for c in cards:
        counts[c] += 1
    
    run_1 = 0
    triplet = 0

    # counts 배열을 복사하여 조작
    temp_counts = counts[:]

    # 먼저 triplet 처리
    for i in range(10):
        while temp_counts[i] >= 3:
            triplet += 1
            temp_counts[i] -= 3

    # 다음으로 run 처리
    for i in range(8):  # 0~7까지 (i, i+1, i+2)
        while temp_counts[i] >= 1 and temp_counts[i+1] >= 1 and temp_counts[i+2] >= 1:
            run_1 += 1
            temp_counts[i] -= 1
            temp_counts[i+1] -= 1
            temp_counts[i+2] -= 1

    if run_1 + triplet == 2:
        print(f'#{test_case} true')
    else:
        print(f'#{test_case} false')