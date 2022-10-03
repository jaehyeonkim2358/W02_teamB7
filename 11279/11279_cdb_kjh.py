import sys
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline().rstrip())

# x가 자연수라면 배열에 x라는 값을 넣는 연산
# x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우

max_heap = [None] * (n)
max_heap[0] = 999999999999
last_index = 0

def push(num):
    global max_heap
    global last_index

    last_index += 1
    max_heap[last_index] = num
    cur = last_index
    while cur != 0:
        if cur//2 != 0 and max_heap[cur//2] < max_heap[cur]:
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
        top = max_heap[1]
        cur = 1
        max_heap[cur] = max_heap[last_index]
        max_heap[last_index] = None
        last_index -= 1
        while cur <= last_list:
            left = cur * 2
            right = cur * 2 + 1
            next_idx = get_next(cur, left, right)
            if max_heap[next_idx] > max_heap[cur]:
                max_heap[next_idx], max_heap[cur] = max_heap[cur], max_heap[next_idx]
                cur = next_idx
            else:
                break
    return top

def get_next(cur, left, right):
    global last_index
    global max_heap

    if right <= last_index:
        return left if max_heap[left] > max_heap[right] else right
    elif left <= last_index:
        return left
    else:
        return cur


while n > 0:
    inputs = int(sys.stdin.readline().rstrip())

    if inputs == 0:
        x = pop()
        sys.stdout.write(f'{x}\n')
    else: 
        push(inputs)
    n -= 1
