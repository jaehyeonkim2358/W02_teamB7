# https://tooo1.tistory.com/441

import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline())
answer = []
print(num)
# 숫자 제거 횟수 체크
k = K
for i in range(N):
    # 제거할 수가 있고, 리스트가 있으면 반복한다.
    # i번째 수보다 작은 리스트의 끝 수를 모두 제거하기 위해서
    while k > 0 and answer:
        if answer[-1] < num[i]:
            # 리스트의 끝 수가 작으면 팝하고 숫자 제거 횟수를 -1 해준다. 
            answer.pop()
            k -= 1
        # 리스트의 끝 수가 더 크면 멈춰준다.
        else:
            break
    # 리스트에 i번째 수를 추가한다. 
    answer.append(num[i])

print(''.join(answer[:N-K]))
