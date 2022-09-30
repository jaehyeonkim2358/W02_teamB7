# 1920: 수 찾기
import sys
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any):
    pl = 0       
    pr = len(a) - 1 
    while True:
        pc = (pl + pr) // 2 
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1     
        else:
            pr = pc - 1     
        if pl > pr: 
            break
    return -1   # 이 놈의 위치 때문이었다......

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    first_list = list(map(int, input().split()))    
    first_list.sort()

    M = int(sys.stdin.readline().strip())
    second_list = list(map(int, input().split()))

    for j in second_list:
        key = j
        idx = bin_search(first_list, key)

        if idx == -1:
            print('0')
        else:
            print('1') 
