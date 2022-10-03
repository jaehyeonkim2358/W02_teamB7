import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
dummy_map = [[0]*n for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    dummy_map[r-1][c-1] = 1
l = int(sys.stdin.readline().rstrip())
dir = [list(sys.stdin.readline().split()) for _ in range(l)]

def game_over(loc, size, snake):
    if loc[0] < 0 or loc[0] > size-1:
        return True
    if loc[1] < 0 or loc[1] > size-1:
        return True
    for s in snake:
        if loc[0] == s[0] and loc[1] == s[1]:
            return True
    return False


s_loc = [[0, 0]]
s_dir = [0, 1]
time = 0
while True:
    time += 1
    next_loc = [s_loc[-1][0]+s_dir[0], s_loc[-1][1]+s_dir[1]]
    if game_over(next_loc, n, s_loc):
        break
    flag = True
    if dummy_map[s_loc[-1][0]][s_loc[-1][1]] == 1:
        dummy_map[s_loc[-1][0]][s_loc[-1][1]] = 0
        flag = False
    s_loc.append(next_loc)
    if s_loc and flag:
        s_loc.pop(0)
    if dir and time == int(dir[0][0]):
        if dir[0][1] == 'D':
            s_dir[0], s_dir[1] = s_dir[1], -s_dir[0]
        else:
            s_dir[0], s_dir[1] = -s_dir[1], s_dir[0]
        dir.pop(0)
    
print(time)
