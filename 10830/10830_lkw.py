import sys
sys.stdin = open("10830/input.txt","r")

n, B = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(lambda x: int(x) % 1000, sys.stdin.readline().split())))    # 원본 배열도 1000으로 나눈 나머지로 저장한다.
                                                                                    # 뒤에서 memo[1] = arr 로 사용하기 때문.
threshold = 100
memo =[None] * (threshold + 1)

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
    if B <= threshold:
        return memo[B]

    h = B//2
    X = go(arr, h, memo, n)
    Y = X if B%2 == 0 else multiply(X, memo[1], n)  # 어차피 원본 행렬은 같기 때문에 B가 짝수면 X와 Y가 같을 것이고, 홀수면 Y에 원본행렬을 한번만 더 곱해주면 된다.
                                                    # B//2 를 통해 반으로 나눴을 때 왼쪽 분기의 값이 도출되면, 오른쪽 분기는 생성할 필요가 없다.
    return multiply(X, Y, n)

memo[1] = arr
for i in range(2, min(threshold+1, B+1)):
    memo[i] = multiply(arr, memo[i-1], n)

for line in go(arr, B, memo, n):
    print(*line, sep=' ')