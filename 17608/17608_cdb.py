# 17608: 막대기

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline())
bar = []
for i in range(N):
    bar.append(int(sys.stdin.readline().strip()))

# 6 9 7 6 4 6 => 맨 마지막인 6이 기준이 됨.
# bar[::-1] 뒤집어서 6 4 6 7 9 6
# 기준: 6
# 근데 마지막 요소를 지웠기 때문에 4 6 7 9 6 이 됨

taller_list = []
taller_list.append(bar[-1])
del bar[-1]
for i in bar[::-1]:
    if i > taller_list[0]:
        if len(taller_list) > 1:
            if i > taller_list[-1]:
                taller_list.append(i)
        else:
            taller_list.append(i)

print(len(taller_list))