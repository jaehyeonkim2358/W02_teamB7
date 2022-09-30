# 고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack:
    # 고정 길이 스택 클래스

    class Empty(Exception):
        # 비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리
        pass

    class Full(Exception):
        # 가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리
        pass

    def __init__(self, capacity: int = 256):
        self.stk = [0] * capacity # 스택 본체
        self.capacity = capacity    # 스택의 크기
        self.ptr = 0        # 스택 포인터
    
    def __len__(self):
        # 스택에 쌓여 있는 데이터 개수를 반환
        return self.ptr
    
    def is_empty(self):
        # 스택이 비어있는지 판단
        return self.ptr <= 0
    
    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value: Any):
        # 스택에 value를 푸시(데이터를 넣음)
        if self.is_full():          # 스택이 가득 차 있는 경우
            raise FixedStack.Full   # 예외 처리 발생
        # 스택이 가득 차 있지 않으면
        self.stk[self.ptr] = value  # 전달받은 value를 배열에 저장
        self.ptr += 1               # 스택 포인터 ptr을 1 증가시킴

    def pop(self, value: Any):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]
    
    def clear(self):
        # 스택을 비움(모든 데이터를 삭제)
        self.ptr = 0
    
    def find(self, valuse: Any):
        # 스택에서 value를 찾아 인덱스를 반환(없으면 -1를 반환)
        for i in range(self.ptr -1, -1. -1):    
            if self.stk[i] == value:
                return i    # 검색 성공
        return -1           # 검색 실패

    def count(self, valuse: Any):
        # 스택에 있는 value의 개수를 반환
        cnt = 0
        for i in range(self.ptr):   # 바닥 쪽부터 선형 검색
            if self.stk[i] == value:    # 검색 성공
                cnt += 1   
        return cnt              

    def __contains__(self, value:Any):
        # 스택에 value가 있는지 판단
        return self.count(value) > 0 

    def dump(self):
        # 덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)
        if self.is_empty():  # 스택이 비어있음
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])


