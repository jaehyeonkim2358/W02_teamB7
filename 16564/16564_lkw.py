import sys
sys.stdin = open("W02/16564/input.txt","r")

def bi_search(length, i, lefted):
    bottom = 0 ; top = length

    while bottom < top:
        mid = (bottom+top)//2 + 1
        fill = i * mid

        if fill <= lefted:      # 아직 더 높일 수 있는 경우
            bottom = mid
        else: # fill > lefted   # 남은 사용 가능 레벨이 부족한 경우
            top = mid - 1

    return bottom

n, K = map(int, input().split())
l = list(map(int, sys.stdin.read().strip().split('\n')))
l.sort()

result = 0
done = False
for i in range(1, len(l)):
    prev_x = l[i-1]
    x = l[i]
    full = i * (x - prev_x)

    if full == K:
        result = x
        done = True
        break
    elif full < K :
        K -= full
        result = x
        continue
    else: # full > K :
        result = prev_x + bi_search(x - prev_x, i, K)
        done = True
        break

if not done:
    print(result + (K//len(l)))
else:
    print(result)
        
