# 10773: 제로

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
K = int(sys.stdin.readline())
money_list = []
sum = 0
def push(num):
    return money_list.append(num)

def pop():
    return money_list.pop()

def is_empty():
    if len(money_list) == 0:
        return 0

while K > 0:
    money = sys.stdin.readline().strip()
    if money == '0':
        pop()
    else:
        push(money)
    K -= 1

if len(money_list) == 0:
    print(is_empty())
else:
    for i in range(len(money_list)):
        sum += int(money_list[i])
    print(sum)