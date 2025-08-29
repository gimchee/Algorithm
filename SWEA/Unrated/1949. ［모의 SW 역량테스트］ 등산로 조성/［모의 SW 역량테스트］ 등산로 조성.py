# 2025-08-29
# SWEA 1949 등산로 조성

'''
DFS + 백트래킹 + 깍기(1회제한)
'''


T = int(input())


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, length, cut_used):
    global max_length

    # 종료 조건 먼저
    if length > max_length:
        max_length = length

    # 방문 행동

    # 상하좌우 이동
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 벽체크 + 방문 안한곳이면
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:

            # 주변 값이 더 낮은 경우 (스타팅 포인트 보다)                
            if arr[nr][nc] < arr[r][c]:

                # 방문 표시 체크 해준다.
                visited[nr][nc] = True

                # 이동하고 재귀 호출을 한다.
                # 그러면 여기 밑에서 계속 낮은곳으로 이동하겠지.
                # 더 낮은곳이 없어지면 함수호출 끝날듯
                dfs(nr, nc, length +1, cut_used)

                # 백트래킹 (방문한거 다시 지우기)
                visited[nr][nc] = False


            # 깍아서 이동하기 + 원상복구

            # 깍은거 아직안쓴경우 
            elif not cut_used:

                # 깍았을때 이동 가능한경우 (주변값 - 깍은값이 내 현재위치보다 작아진경우)
                # 1 ~ K 까지 깍을 수 있으므로
                for depth in range(1, K + 1):
                    
                    # 깍기 전 높이 저장
                    original = arr[nr][nc]   
                    
                    # 주변값을 1~K 까지 깍기 (음수도 가능하니까 근냥 상관없이 깍기)
                    arr[nr][nc] -= depth

                    # 깍은게 더 작은경우
                    if arr[nr][nc] < arr[r][c]:
                    
                        # 방문체크
                        # 여기도 깍아서 움직인거니까 일단 방문체크
                        visited[nr][nc] = True

                        # 한 싸이클 마찬가지로 끝냈으니까.
                        # 다시 재귀함수 호출함 
                        # 근데 cut 써먹었으니까, True 로 바꿔서 재귀 호출한다.
                        # 한번 썼기 때문에 여기 if문은 못들어 오는듯?>

                        dfs(nr, nc, length +1, True)

                    # 함수호출이 끝나고 다시 돌아올때,
                    # 원상복구를 시켜준다 (백트래킹)
                    visited[nr][nc] = False

                    # 마찬가지로 백트래킹 - 복원시켜준다.
                    arr[nr][nc] = original

    # 재귀 호출





for test_case in range(1, T+1):

    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    

    # 봉우리 최대값 찾기
    max_value = 0    
    for i in range(N):
        for j in range(N):            
            if arr[i][j] > max_value:
                max_value = arr[i][j]


    # 시작점 위치 찾기
    start_points = []    
    for i in range(N):
        for j in range(N):            
            if arr[i][j] == max_value:
                start_points.append([i,j])


    # 최대 길이 변수
    max_length = 0
    
    # 방문체크용 입력값과 똑같은 크기 배열 만들기
    visited = [[False] * N for _ in range(N)]

    for r, c in start_points:

        # 맨 처음 시작점 방문 체크함
        visited[r][c] = True
        dfs(r, c, 1, False)

        # 백트래킹함
        # 왜냐? 스타팅포인트가 여러개 이기 때문에
        # 원상복구를 시켜줘야 한다.
        visited[r][c] = False

    print(f"#{test_case} {max_length}")

