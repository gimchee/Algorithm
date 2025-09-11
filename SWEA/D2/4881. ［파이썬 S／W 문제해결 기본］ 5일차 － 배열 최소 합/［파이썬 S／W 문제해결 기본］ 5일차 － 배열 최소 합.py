# 2025-09-11
# SWEA 4881 배열최소합


# dfs 구현하기
def dfs(r, current_sum):

    global min_sum 
    # 가지치기
    if current_sum >= min_sum:
        return
    
    # 종료조건
    if r == N:
        # 최소값을 업데이트 하기
        min_sum = min(min_sum, current_sum)
        return

    # 재귀
    for c in range(N):
        
        # 방문을 아직 안했다면
        if visited[c] == 0:
            # 방문처리 하기
            visited[c] = 1
            # r~ 끝까지 돌기, sum은 누적해서 업데이트
            # 재귀
            dfs(r+1, current_sum + arr[r][c])
            
            # 방문 다시 원상복구하기 
            visited[c] = 0

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 1000000

    visited = [0] * N

    dfs(0,0)

    print(f'#{tc} {min_sum}')