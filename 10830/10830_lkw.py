import sys
sys.stdin = open("10830/input.txt","r")

n, B = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(lambda x: int(x) % 1000, sys.stdin.readline().split())))

threshole = 100
memo =[None] * (threshole + 1)

def multiply(X, Y, n):
    result = []
    for i in range(n):          # 행
        result.append([])
        for j in range(n):      # 열
            atom = 0
            for k in range(n):  # 원소 순서
                atom += X[i][k] * Y[k][j]
            result[i].append(atom%1000)
    
    return result

def go(arr, B, memo, n):
    if B <= threshole:
        return memo[B]

    h = B//2
    X = go(arr, h, memo, n)
    Y = X if B%2 == 0 else multiply(X, memo[1], n)
    return multiply(X, Y, n)

memo[1] = arr
for i in range(2, min(threshole+1, B+1)):
    memo[i] = multiply(arr, memo[i-1], n)

for line in go(arr, B, memo, n):
    print(*line, sep=' ')