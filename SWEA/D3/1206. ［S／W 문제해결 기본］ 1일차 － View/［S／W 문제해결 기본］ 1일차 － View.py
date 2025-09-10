# 2025-09-10
T = 10

for tc in range(1, T+1):

    _ = input()
    arr = list(map(int, input().split()))

    temp = 0
    my_sum = 0
    for i in range(2, len(arr)-2):

        temp = min(arr[i]-arr[i-2],arr[i]-arr[i-1], arr[i]-arr[i+1], arr[i]-arr[i+2])

        if temp > 0:
            my_sum += temp
        
        temp = 0

    print(f'#{tc} {my_sum}')