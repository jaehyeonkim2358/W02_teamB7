import sys

n = int(sys.stdin.readline().rstrip())
points = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])

def solution(s, e):
    if e - s <= 1:
        return get_distance(points[s], points[e])
    if e - s == 2:
        return min(get_distance(points[s], points[s+1]), get_distance(points[s+1], points[e]), get_distance(points[s], points[e]))

    m = (s + e) // 2

    min_dist = min(solution(s, m), solution(m+1, e))

    mid_range = abs(m - get_index(points, min_dist, points[m], s, e))
    new_start = m-mid_range if m >= mid_range else 0
    new_end = m+mid_range if m+mid_range <= e else e
    new_arr = sorted(points[new_start:new_end+1], key=lambda x: x[1])

    min_dist = sweep_up(new_arr, min_dist)
    return min_dist


def sweep_up(new_arr, min_dist):
    for i in range(len(new_arr)):
        for j in range(i+1, len(new_arr)):
            y_dist = (new_arr[i][1]-new_arr[j][1])**2
            if y_dist >= min_dist:
                i = j-1
                break
            tmp_dist = (new_arr[i][0]-new_arr[j][0])**2 + y_dist
            if tmp_dist < min_dist:
                min_dist = tmp_dist
                i = j-1
                break

    return min_dist


def get_index(arr, key, target, start, end):
    s = start
    e = end
    while s < e:
        m = (s + e) // 2 + 1
        if abs(arr[m][0]-target[0])**2 > key:
            e = m - 1
        else:
            s = m
    return e


def get_distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


sys.stdout.write(f'{solution(0, n-1)}')