import sys
sys.stdin = open("2110/input.txt","r")

n, c = map(int, input().split())
l = list(map(int, sys.stdin.read().strip().split('\n')))

l.sort()    # 집의 좌표 배열을 오름차순으로 정렬

# 지금 찾고자 하는 값은 '거리'라는 숫자이다.
# 탐색을 하는 공간은 0 + 양의수직선([0,1,2,3,4, ... ,최대거리]) 이다. 
# 지금 mid보다 큰 범위로 갈것인지, 작은 범위로 갈 것인지는 현재 mid라는 거리를 사용한 sulchi의 반환값(cnt)이 '충분한지'(c보다 같거나 큰지) 이다.
# cnt가 c보다 같거나 큰 경우(충분히 설치된 경우),
# start = mid(=attempt 지금 시도한 거리) 해줌으로써, 범위를 오른쪽으로 이동(보다 큰 거리를 찾는다.)하고,
# 지금은 가능한 큰값(긴 거리)를 찾아야 하니까, 나중에 거리를 줄여야 할 때 최소한 start까지는 '충분하다'는 것을 보장해준다.
def bi_search(start, end, c):
    while start < end:
        attepmt = (start+end)//2 + 1
        
        cnt = sulchi(l, attepmt)
        if cnt >= c:               # 너무 많이 설치됨. 거리를 늘려도 됨.
            start = attepmt
        else: # cnt < c             # 너무 적게 설치됨. 거리를 줄여야 함.
            end = attepmt - 1
    
    return start

def sulchi(l, d):
    root = l[0]
    count = 1   # root에 일단 설치.
    for h in l[1:]:
        if d <= h - root: # root부터 현재 h 까지의 거리가 최소거리 d 보다 크거나 같을 때. 즉 설치할 수 있을 때.
            count += 1
            root = h
        else:
            continue
    
    return count

# start = 1도 되나? -> 1도 됨. 1이면 sulchi의 count가 집 개수가 된다. c는 집 개수보다 같거나 작기 때문에 1이하로 떨어질 경우가 없다.
print(bi_search(0, l[-1] - l[0], c))

        