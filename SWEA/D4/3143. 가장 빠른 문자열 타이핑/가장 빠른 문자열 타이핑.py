# 2025-09-04
# SWEA 3143. 가장 빠른 문자열 타이핑

T = int(input())
for test_case in range(1, T+1):
    
    A, B = input().split()

    count = 0

    # A에서 B의 개수 체크
    count = A.count(B)

    # A에서 B를 제거한다.
    for _ in range(len(A)-len(B)):

        # B가 A에 있으면
        if B in A:
            result = A.replace(B,"")


    count += len(result)
    print(f'#{test_case} {count}')
