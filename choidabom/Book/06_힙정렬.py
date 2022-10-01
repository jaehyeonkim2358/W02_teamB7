# 힙 정렬(Heap sort)란 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법으로, 
# 내림차순 정렬 => 최대 힙 구성, 오름차순 정렬 => 최소 힙 구성

def heap_sort(unsorted):
    n = len(unsorted)
    #최대 힙 만들기
    #최소힙은 부등호만 반대로 바꿔주면 됨
    for i in range(1, n):
        child = i
        while child != 0:
            parent = (child-1)//2
            if unsorted[parent] < unsorted[child]:
                unsorted[parent], unsorted[child] = unsorted[child], unsorted[parent]
            child = parent #최대값이 루트까지 도달 할 수 있도록

    #힙 만들기
    for node in range(n-1, -1, -1):
        #루트 노드와 마지막 노드를 교환
        #값이 큰 순서대로 힙의 끝에 저장됨
        unsorted[0], unsorted[node] = unsorted[node], unsorted[0]
        parent = 0
        child = 1

        # 정렬이 미완료 된 노드들 사이에서
        # 마지막 노드 자리리 보내준 루트 노드를 제외한 가장 큰 값을 찾고
        # 루트 노드 자리로 온 마지막 노드의 자리 찾기
        while child < node:
            child = parent*2 + 1
            #마지막 노드 자리로 보낸 루트 노드를 제외한 가장 큰 노드를 찾기 위해
            if child < node-1 and unsorted[child] < unsorted[child+1]:
                child += 1
            #마지막 노드 자리로 보낸 루트 노드를 제외한 가장 큰 노드를 루트 자리로 보내기 위한 과정
            if child < node and unsorted[parent] < unsorted[child]:
                unsorted[parent], unsorted[child] = unsorted[child], unsorted[parent]

            parent = child

    return unsorted



if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    print(heap_sort(arr))