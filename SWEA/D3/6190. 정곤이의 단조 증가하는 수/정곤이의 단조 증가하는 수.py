# 2025-09-09
# SWEA 6190 정곤이의 단조 증가하는 수

'''
단조란 그숫자의 자리수가 증가하는 수를 말함.
'''

def danjo(n):

    str_n = str(n)


    for i in range(len(str_n)-1):

        if str_n[i] > str_n[i+1]:
            return -1

    return n


T = int(input())

multiple_arr = []

for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int, input().split()))

    max_val = -1
    # 곱하는 경우의 수 만들기
    for i in range(N-1):
        for j in range(i+1,N):
            
            temp = arr[i] * arr[j]
            # 곱셈 경우의 수 만들어서 새로운 리스트에 append
            if danjo(temp) != -1:
                max_val = max(temp,max_val)

    print(f'#{tc} {max_val}')
