import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def solution(target, key):
    s = 0
    e = max(target)
    while s < e:
        m = (s + e) // 2 + 1
        if get_height(target, m) < key:
            e = m - 1
        else:
            s = m
    return s


def get_height(target, h):
    sum = 0
    for t in target:
        sum += (t-h if t>h else 0)
    return sum


sys.stdout.write(f'{solution(trees, m)}')