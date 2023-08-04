# deque로 스택 구현하기
'''
deque?
맨 앞과 맨 끝 양쪽에서 원소를 추가 및 삭제하는 자료구조인
덱을 구현하는 컨테이너!
'''

from typing import Any
from collections import deque

class Stack:
    def __init__(self, maxlen: int=256)-> None:
        self.capacity= maxlen
        # maxlen: deque의 최대 크기를 나타내는 속성으로 읽기전용. 크기 제한이 
        #없으면 None임
        self.__stk = deque([], maxlen)
    
    def __len__(self)-> int:
        return len(self.__stk)
    
    def is_empty(self)-> bool:
        return not self.__stk
    
    def is_full(self)-> bool:
        return len(self.__stk)== self.__stk.maxlen
    def push(self, value: Any)-> None:
        self.__stk.append(value)#append: deque의 맨 끝에 x를 추가
        
    def pop(self)-> Any:
        return self.__stk.pop()
    
    def peek(self)-> Any:
        return self.__stk[-1]
    def clear(self)-> None:
        self.__stk.clear()
    def find(self, value: Any)-> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1
    def count(self, value: Any)-> int:
        return self.__stk.count(value)
    # self.__stk: 파이썬 클래스 내부에서 스택 데이터를 가리키는 변수
    #__를 쓰면 private변수로 간주하자는 암묵적인 룰이 있다.
    #스택에 포함되어 있는 value의 개수 반환
    def __contains__(self, value: Any)-> bool:
        return self.count(value)
    def dump(self)-> int:
        print(list(self.__stk))
    
    