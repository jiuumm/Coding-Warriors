from typing import Any

class FixedStack:
    class Empty(Exception):
        
        pass
    class Full(Exception):
        pass
    
    def __init__(self, capacity: int=256) ->None:
        #스택 전체 크기: capacity
        #포인터: 스택에 쌓여있는 데이터 수 
        self.stk = [None]*capacity
        self.capacity = capacity
        self.ptr=0
    
    def __len__(self) -> int:
        #스택에 쌓여있는 데이터 수(포인터) 반환(int 형)
        return self.ptr
    #스택이 비어있는가?
    def is_empty(self) ->bool:
        return self.ptr <=0
    #스택이 꽉 찼는가?
    def is_full(self) ->bool:
        return self.ptr >= self.capacity
    
    def push(self, value: Any) -> None:
        #스택 차면 예외 발생
        if self.is_full():
            raise FixedStack.Full
        #아니면 push!
        self.stk[self.ptr]= value
        self.ptr+=1
    def pop(self) ->Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -=1
        return self.stk[self.ptr-1]

        #스택을 완전히 비움
    def clear(self) -> None:
        self.ptr=0
    
    def find(self, value: Any)-> Any:
        for i in range(self.ptr-1 , -1, -1):
            if self.stk[i]==value:
                return i
            return -1 #검색 실패시
        '''
        self.ptr-1에서 시작해서 인덱스가 -1씩 줄어들다가
        인덱스 0까지 !(종료값이 -1인 이유는 원래 마지막+1로 읽기 때문)
        '''
    def count(self, value: Any)-> int:
        c=0
        #스택의 바닥부터 검사
        for i in range(self.ptr):
            if self.stk[i]==value:
                c+=1
        return c
    
    def __contains__(self, value: Any)-> bool:
        return self.count(value)>0
    '''
    in키워드와 함께 사용이 가능함
    ex)
    lst = [1,2,3,4]
    print(3 in lst)
    이렇게 하면 True가 반환됨.
    '''
    def dump(self)-> None:
        if self.is_empty():
            print("스택 비어있음")
        else:
            print(self.stk[:self.ptr]) #스택 비어있지 않으면 스택 안에 있는 모든 값들 출력
            
        