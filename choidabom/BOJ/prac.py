import sys
N = int(sys.stdin.readline())

num_list = []
for i in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    print(input)
    num_list.append(input)

print(num_list)