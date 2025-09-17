import heapq


def dijkstra(start_node, num_vertices, adj_list):
    """
    Dijkstra 알고리즘 (우선순위 큐 활용)
    """
    # 1. 초기화 작업
    # 1번 정점으로부터 모든 정점까지의 거리를 기록할 리스트
    INF = float('inf')
    distance = [INF] * (num_vertices + 1)

    # 우선순위 큐(최소 힙) 생성
    priority_queue = []

    # 2. 시작 노드 처리
    # 2.1 시작 노드까지의 거리는 0으로 설정
    # 2.2 우선순위 큐에 삽입
    # glqdpsms (거리, 노드번호) 순서러 저장, 최소힙이기 때문에 나중에 거리가 짧은 순으로 꺼내기 위함
    distance[start_node] = 0
    heapq.heappush(priority_queue, (0, start_node))

    # 3. 메인 과정 (큐가 빌 때까지 반복)
    while priority_queue:
        # 4. 현재까지 가장 거리가 짧은 노드를 힙에서 꺼냄
        current_dist, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드라면 (더 짧은 경로를 이미 발견했다면) 무시
        # 가지치기
        # 과거것이 더 작은거면, (현재보다) 의미가 없으니까
        if distance[current_node] < current_dist:
            continue

        # 5. 현재 노드와 인접한 노드들을 확인
        for adj_node, weight in adj_list[current_node]:
            
            # 새로운 경로(거리)
            new_dist = current_dist + weight

            # 6. 새로운 경로가 기존 경로보다 더 짧으면 갱신
            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                # 갱신된 정보를 우선순위 큐에 추가
                heapq.heappush(priority_queue, (new_dist, adj_node))

    return distance

# --- 실행 예시 ---
T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    start = 0
    adj_list = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))


    # 다익스트라 알고리즘 실행
    shortest_distances = dijkstra(start, V, adj_list)

    # 1번 노드에서 각 노드까지의 최단 거리
    print(f'#{tc} {shortest_distances[V]}')  # [inf, 0, 2, 5, 1, 2, 4]