# 2025-09-04
# SWEA 5188. 최소합

# 이동은 아래 or 오른쪽
# 더 값이 작은걸로 이동하고 누적합 구해서 출력

# 아래, 오른쪽
dr = [1, 0]
dc = [0, 1]

def dfs(r, c, temp):

    global result
    
    # 종료조건
    if r == N-1 and c == N-1:
        result = min(result,temp)
        return

    # 탐색
    for i in range(2):

        nr = r + dr[i]
        nc = c + dc[i]
        # 벽체크
        if 0 <= nr < N and 0 <= nc < N :
            # 재귀호출      
            dfs(nr, nc , temp + arr[nr][nc])

    

T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 10000

    # 시작점 넣기
    dfs(0,0,arr[0][0])

    print(f'#{test_case} {result}')