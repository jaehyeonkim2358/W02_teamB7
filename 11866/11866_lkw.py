from collections import deque
import sys
sys.stdin = open("11866/input.txt","r")

n, k = map(int, input().split())

def yose(n,k):
    q = deque(range(1,n+1), maxlen=n)
    l = []
    while q:
        q.rotate(-k)
        l.append(q.popleft())
    return l

print('<', end='')
print(*yose(n,k-1), sep=', ', end='')
print('>', end='')
