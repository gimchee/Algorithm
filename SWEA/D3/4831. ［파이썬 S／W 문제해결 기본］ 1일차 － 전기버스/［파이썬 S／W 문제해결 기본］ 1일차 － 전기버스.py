# 전기 버스

# 체크1


# 1. count배열 만들기 (충전소 인덱스 접근용)
# 2. 현재위치에서 끝까지 반복한다
# 3. 최대치 까지 다음 스텝을 만들어 놓은 다음
# 4. 다음 스텝에서 현재위치로 돌아오는 반복문을 돌려서 첫 번째 정류장을 현재 위치로 업데이트한다.
# 5. 업데이트와 동시에 충전 횟수 업데이트
# 6. 반복문을 돌렷는데, 정류장 위치를 못찾은경우
# 6.1 다 돌린경우 while문 탈출



T = int(input())

for test_case in range(1, T+1):

    # K : 한번에 이동할 수 있는 거리
    # N : 종점 
    # M : 정류장 개수
    K, N, M = map(int, input().split())
    
    # 충전기 정류장 번호
    chargers = list(map(int, input().split()))

    count = [0] * (N+1)

    # 정류장 만들기
    for i in chargers:
        count[i] = 1


    now = 0
    next_ = 0
    charge_count = 0

    # 반복하기
    # 현재위치가 끝까지 갈 때 까지 반복한다
    while now < N: 

        # 다음에 갈 수 있는 최대치를 선언한다.
        next_ = now + K

        # 아직 끝까지 한게 아니라면
        if next_ < N:
            
            for i in range(next_,now, -1):

                if count[i] == 1:
                    now = i
                    charge_count += 1
                    # 이번 루프 탈출 -> 다음 while문 진행
                    break
            
            # break문이 실행되지 않은 경우 while문 전체를 탈출한다.
            # 종점까지 가기전에 break가 실행되지 않은 경우( 충전소를 들리지 못하는 경우) 탈출
            else:
                # 가다가 중간에 충전 못하는 경우에
                # 충전횟수 늘어났으므로, 다시 초기화 시켜
                # 충전이 불가능하다고 알린다.
                charge_count = 0
                break

        # 끝까지 다 도달한 경우
        # while 탈출
        else:
            break

    
    print(f'#{test_case} {charge_count}')