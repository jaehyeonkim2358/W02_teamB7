# 힙 인덱스 구조.
# 계산의 용이함을 위해 원소 개수 n 보다 1 큰 배열을 만들어, 최종 루트 인덱스를 1부터 시작하게 한다.
# [None, *(1), *(2), *(3), ..., *(n)]
# 원소 인덱스 i에서
# - 부모 인덱스 : i//2
# - 왼쪽 자식 : 2*i
# - 오른쪽 자식 : 2*i + 1

def heap_sort(l):
    
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

    # 정렬할 배열 전체 heapify.
    n = len(l)-1    # 배열 맨 앞 None 때문에 -1 해준다.
    for i in range(n//2, 0, -1):  # 가장 '마지막 부모' 부터 시작해서 최고 root까지 반복. down_heap은 root 밑의 트리들이 heap을 만족한다고 전제한다. 그래서 가장 마지막 부모부터 시작.
        down_heap(l, i, n)

    # 하나씩 뽑아서 배열 마지막에 넣고 트리에서 제외한 뒤 남은 트리 최상단 root(뽑은 노드와 자리 바꾼 노드)를 down_heap.
    for i in range(n, 0, -1):
        l[1], l[i] = l[i], l[1]
        down_heap(l, 1, i-1)    # 항상 최상단(1) 노드를 다운 힙.

l = [None]+[(-x,x) for x in [10,9,5,8,3,2,4,6,7,1]]
heap_sort(l)
print(l)