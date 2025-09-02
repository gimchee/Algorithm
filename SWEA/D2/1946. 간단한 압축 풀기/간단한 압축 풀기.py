# 2025-09-02
# SWEA 1946 간단한 압축 풀기


T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    my_str = ''

    for _ in range(N):
        Ci, Ki = input().split() 

        my_str += "".join(Ci * int(Ki))

        # 너비가 10으로 끊어야 .

    
    print(f'#{test_case}')
        
    # 0, 10, 20 : i값
    for i in range(0, len(my_str), 10):
        
        # 0 - 10 / 10 ~ 20 / 20 ~ 30 이런식
        print(my_str[i:i+10])