# 2025-08-27
# 백준 13458 시험감독

'''
# N개의 시험장
# i번 시험장 -> 응시자수 Ai 명
# 총감독관 : 감시가능 응시자 B명
# 부감독관 : 감시 가능 응시자 C명

# 총감독관은 1명만, 부감독관은 여러 명 가능
# 필요한 감독관 수의 최솟값은 ?
'''
import math
import sys
# sys.stdin = open("input_13458.txt")
# 시험장의 개수 : N
N = int(input())

# 각 시험장의 응시자수 : Ai
Ai = list(map(int,input().split()))

# 총 감독관 : B
# 부 감독관 : C
B,C = map(int, input().split())


count = 0



for i in range(len(Ai)):
    Ai[i] = Ai[i] - B
    count += 1
# 총감독관의 범위가 부 감독관 보다 크면

# 부 감독관이 얼마나 필요한지 계산한다.
# 응시자수에 대해 나누고, 소수점은 올림처리해서 계산한다.
for i in range(len(Ai)):
    if Ai[i] > 0:
        count += math.ceil(Ai[i] / C)

    
print(count)        
                