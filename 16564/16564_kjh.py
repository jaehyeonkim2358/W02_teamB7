from re import L
import sys

n, k = map(int, sys.stdin.readline().split())
level = list()
while n > 0:
    level.append(int(sys.stdin.readline().rstrip()))
    n -= 1

level.sort()

def solution(target, key):
    s = min(target)
    e = max(target) + key
    while s < e:
        m = (s+e)//2 + 1
        if get_dest_level(target, m, key):
            s = m
        else:
            e = m - 1
    return e


def get_dest_level(target, dest_lev, key):
    for t in target:
        if t >= dest_lev:
            break
        else:
            key -= (dest_lev-t)
        if key < 0:
            return False
    return True


print(solution(level, k))