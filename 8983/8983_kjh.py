import sys

def main():
    m, n, l = map(int, sys.stdin.readline().split())

    spot = sorted(list(map(int, sys.stdin.readline().split())))

    count = 0
    def solution(animal, l):
        # global count
        s = 0
        e = len(spot)-1
        while s < e:
            m = (s+e) // 2
            # spot[m]과 동물의 거리가 l보다 클경우
            if abs(spot[m]-animal[0]) + animal[1] > l:
                # 사대의 x좌표가 동물의 x좌표보다 클 경우
                if spot[m] > animal[0]:
                    e = m - 1
                # 사대의 x좌표가 동물의 x좌표보다 작을 경우
                # :: 같을 경우는 존재하지 않음 
                # (입력 단계에서 y>l인 경우를 받지 않았기 때문에, 동물과 사대 사이의 거리가 l보다 크면서 x좌표는 같을 경우는 존재하지 않는다.)
                else:
                    s = m + 1
            # spot[m]과 동물의 거리가 l보다 작거나 같을경우
            else:
                # 사냥 가능하므로 count를 1 증가시키고 종료
                # count += 1
                return 1
        if abs(spot[e]-animal[0]) + animal[1] <= l:
            # count += 1
            return 1
        else:
            return 0

    # 동물 좌표를 입력 받는대로 탐색
    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        # y좌표가 l보다 작거나 같을때만 탐색 진행
        if tmp[1] <= l:
            count += solution(tmp, l)


    sys.stdout.write(f'{count}')

if __name__ == '__main__':
    main()