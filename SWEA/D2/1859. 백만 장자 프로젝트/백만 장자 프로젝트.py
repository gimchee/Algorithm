# 2025-09-02
# SWEA 1859 백만 장자 프로젝트



T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    arr = list(map(int,input().split()))


    max_value = 0

    profit = 0

    for i in reversed(arr):
        if i > max_value:
            max_value = i
        else:
            profit += (max_value - i)
    
    print(f'#{test_case} {profit}')


    ''' 
    뒤에서 부터 최대값을 업데이트를 해가며
    앞이 뒤보다 작은 경우에만 차이를 구한다.
    앞이 뒤보다 크면 최대값을 업데이트한다.
    '''