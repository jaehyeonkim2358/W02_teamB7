# 2805: 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

# start와 end가 같아질 때까지 반복
while start <= end:
    mid = (start + end) // 2
    tree = 0    # 잘린 나무 합
    # 나무 자르기
    # trees => [20, 15, 10, 17]
    for i in trees:
        # 나무의 높이가 절단기 높이보다 크다면
        if i > mid:
            tree += i - mid

    # 원하는 나무 높이보다 덜 잘렸으면
    if tree < m:
        end = mid - 1
    # 원하는 나무 높이보다 더 많이 잘렸으면
    else:
        start = mid + 1

print(end)

