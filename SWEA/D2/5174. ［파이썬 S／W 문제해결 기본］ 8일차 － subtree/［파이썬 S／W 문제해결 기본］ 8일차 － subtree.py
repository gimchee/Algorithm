


# 전위 순회 함수
# 루트 -> 왼쪽 -> 오른쪽 순서

def preorder(node):
    global count
    if node != 0:

        count += 1
        preorder(left[node])
        preorder(right[node])
    return count
# 중위순회 함수
# 왼쪽 -> 루트 -> 오른쪽

def inorder(node):

    if node != 0:

        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])

# 후위순회 함수
# 왼쪽 -> 오른쪽 -> 루트

def postorder(node):

    if node != 0:

        postorder(left[node])
        postorder(right[node])
        print(node, end=' ')






T = int(input())

for test_case in range(1, T+1):

    E, N = map(int, input().split())

    node = list(map(int, input().split()))


    # 왼쪽 자식 정보
    left = [0] * (E + 2)

    # 오른쪽 자식 정보
    right = [0] * (E + 2)


    # left, right로 나누기

    for i in range(E):
        parent, child = node[i * 2], node[i * 2 + 1]

        # 왼쪽부터 채우기.
        # 오른쪽 부터 해도 되지 않나??
        # --> 문제 입력이 왼쪽 먼저이기 때문에, 왼쪽 먼저 해야함
        if left[parent] == 0:
            left[parent] = child

        # 왼쪽에 이미 할당 했으면 오른쪽에 할당한다.
        else:
            right[parent] = child

    count = 0

    print(f'#{test_case} {preorder(N)}')
