import sys

n = int(sys.stdin.readline().rstrip())

while n > 0:
    ps = sys.stdin.readline().rstrip()
    flag = True
    count = 0
    for p in ps:
        if p == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            flag = False
            break
    if flag and count == 0:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
    n -= 1