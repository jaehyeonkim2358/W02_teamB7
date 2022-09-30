import sys

n = int(sys.stdin.readline().rstrip())

max_heap = [None] * (4 * n)
max_heap[0] = 999999999999
last_index = 0

def add(num):
    global max_heap
    global last_index

    last_index += 1
    max_heap[last_index] = num
    cur = last_index
    while cur != 0:
        if max_heap[cur//2] < max_heap[cur]:
            max_heap[cur], max_heap[cur//2] = max_heap[cur//2], max_heap[cur]
            cur //= 2
        else:
            break    


def pop():
    global max_heap
    global last_index
    if last_index == 0:
        return 0
    else:
        v = max_heap[1]
        cur = 1
        max_heap[cur] = max_heap[last_index]
        max_heap[last_index] = None
        last_index -= 1
        while cur <= last_index:
            left = cur * 2
            right = cur * 2 + 1
            next = _get(cur, left, right)
            if max_heap[next] > max_heap[cur]:
                max_heap[next], max_heap[cur] = max_heap[cur], max_heap[next]
                cur = next
            else:
                break
        return v


def _get(cur, index1, index2):
    global last_index
    global max_heap

    if index2 <= last_index:
        return index1 if max_heap[index1] > max_heap[index2] else index2
    elif index1 <= last_index:
        return index1
    else:
        return cur
    

while n > 0:
    k = int(sys.stdin.readline().rstrip())
    if k == 0:
        x = pop()
        sys.stdout.write(f'{x}\n')
    else:
        add(k)
    n -= 1