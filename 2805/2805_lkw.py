import sys
sys.stdin = open("2805/input.txt","r")

n, m = map(int, input().split())
l = list(map(int, input().split()))

top = max(l)
bottom = 0
while bottom <= top:        # 등호를 붙이지 않으면 bottom 과 top이 같아질 때의 cut(=bottom=top)을 해보지 않고 끝내게 된다.
    cut = (top+bottom)//2
    load = 0
    for namu in l:
        if namu > cut:
            load += namu - cut
            if load > m : break
    if load == m:
        break

    if load < m:         # 너무 적게 베었을 때
        top = cut-1
    else: # load > m     # 너무 많이 베었을 때
        bottom = cut+1

print(cut-1 if load < m else cut)
