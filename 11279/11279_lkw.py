import sys
sys.stdin = open("11279/input.txt","r")

# 이 힙 함수들은 max_heap을 위한 함수이다.
def pop_heap(l):
    if len(l) == 1 :
        return 0
    elif len(l) == 2:
        return l.pop()[1]

    root_node = l[1]
    l[1] = l.pop()

    down_heap(l, 1, len(l)-1)

    return root_node[1]


def down_heap(l, root, n):  # root 밑의 트리들은 모두 heap을 만족하다는 가정하에 실행되는 함수이다. root밑 힙 구조 안에 root를 어디에 넣을 것인지 판단하고 넣는 함수이다. 'down_heap'
        temp = l[root]
        rootkey = temp[0]   # 노드 비교 기준인 key를 받는다. 노드 : (key, value)
        child = 2 * root    # 왼쪽 자식

        while child <= n :  # 현재 root 에서 계산된 child가 n을 넘는다면, 현재 root가 리프노드라는 뜻이기에 해당 조건문이 존재.
            if child < n and l[child][0] < l[child+1][0]:   # child < n 가장 하단 트리에서 자식이 하나 있는 경우에 child == n(전체 노드 개수)이 됨.
                                                            #   따라서, 왼쪽 자식 오른쪽 자식 고를 필요 없음
                child += 1 # 오른쪽 자식으로 변경

            if rootkey > l[child][0] :
                break    # 선택된 자식 (둘 중 큰 자식) 보다 루트가 크다면 더이상 진행할 필요가 없다. 그 밑은 이미 heap이기 때문에.
            else:
                l[child//2] = l[child]  # child//2 는 부모. 하나 밀어 올린다. 부모 노드는 이미 temp에 저장 중.
                child *= 2              # child의 왼쪽 자식으로 이동.

            l[child//2] = temp # 지금 child는 마지막에 root를 삽입해야 하는 노드의 child이기 때문에 //2를 한 인덱스를 준다.

def push_heap(l, node):
    up_heap(l, node)

def up_heap(l, node):
    l.append(node)  # 맨 밑에 삽입할 node를 두고 기준에 맞게 올린다(upheap).

    nodekey = node[1]
    child = len(l)-1

    while child > 1 and nodekey > l[child//2][1]:
        l[child] = l[child//2]
        child //= 2
    l[child] = node

n = int(sys.stdin.readline())
l = [None]
for _ in range(n):
    v = int(sys.stdin.readline())
    
    if v == 0:
        print(pop_heap(l))
    else :
        push_heap(l, (v,v))