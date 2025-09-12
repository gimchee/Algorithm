
def recur(cnt, total_height):

    global min_answer
    
    if total_height >= B:  # 가지치기 : B이상이면 더이상 x
        min_answer = min(min_answer, total_height)
        return

    if cnt == N: #  N명을 모두 고려함
        return
    
    recur(cnt + 1, total_height + heights[cnt])  # 탑에 포함 시키는 경우
    recur(cnt + 1, total_height)  # 탑에 포함 안 시키는 경우
    # 우리가 알고 싶은건 높이이다.

    # 종료조건 : N명의 모든 점원을 고려했을 때
    # - 가지치기 : 탑을 쌓았는데 이미 높이가 B이상이면 더이상 쌓을 필요가 없다
    # 가지의 수 
    # - 점원을 탑에 포함 시키는 경우 or 안시키는 경우


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))

    min_answer = 210000

    recur(0,0)

    print(f'#{tc} {min_answer-B}')