# 16564: 히오스 프로게이머

# 기본적으로 나무자르기 문제와 같은 개념 (잘라야 하는 나무의 양 = 레벨 업해야하는 총량)
# 레벨업하는 총량이 올릴 수 있는 레벨의 총합(k)을 넘어가지 않는 선에서 최대 높이를 찾는다.
# 어차피 남는 레벨을 다 써도 min(Xn)은 똑같을 것

import sys
sys.stdin = open('input.txt', 'r')
# N개의 캐릭터, 각 캐릭터의 레벨 Xi
# 올릴 수 있는 레벨 총합 K
N, K = map(int, sys.stdin.readline().split())
level = sorted([int(sys.stdin.readline().rstrip()) for i in range(N)])
# 악 !!! sorted 안 해서 값이 안 나오는 것이었다...

def solution(targets, k, n):
    # 최저점을 가장 낮은 레벨(min(level))
    # 최고점은 max(level) 값에 k//n을 더해준다.
    # 이 둘의 평균을 t_value로 잡아서 이분탐색 시작
    lowest, highest = min(targets), max(targets) + k//n
    while lowest <= highest: 
        t_value = (lowest + highest) // 2
        total = 0
        for target in targets:
            if t_value > target:
                total += t_value - target
            else:
                break

        # total: 레벨업하는 총량
        # k: 레벨의 총합(K)
        if total > k:
            highest = t_value - 1
        elif total == k:
            return t_value
        # 레벨의 총합 K보다 적게 올릴 수도 있기에 t_value를 temp에 넣어줌
        else:
            temp = t_value
            lowest = t_value + 1
    return temp

sys.stdout.write(f'{solution(level, K, N)}')
