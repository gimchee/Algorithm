# 2025-09-02
# SWEA 5356. 의석이의 세로로 말해요

T = int(input())

for test_case in range(1, T+1):

    name = [list(input()) for _ in range(5)]
    

    max_val = 0
    for i in range(5):
        max_val = max(len(name[i]),max_val)


    # try-except로 indexerror 그냥 무시하고 넘어감
    # 없는 글자 넘어감
    print(f'#{test_case}', end=' ')
    for i in range(max_val):
        for j in range(5):
            try:
                print(name[j][i], end = '')
            except IndexError:
                pass
    print()        