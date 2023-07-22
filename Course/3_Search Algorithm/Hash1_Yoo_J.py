
#체인법으로 해시함수 만들기
from __future__ import annotations
from typing import Any, Type
import hashlib
#해시를 구성하는 노드
class Node:

    def __init__(self, key:Any, value :Any, next: Node)->None:

        self.key = key
        self.value = value
        self.next = next

class ChainedHash:

    def __init__(self, capacity : int)->None:
        self.capacity = capacity #해시 테이블의 크기
        self.table = [None]*self.capacity

    #해시값 return해주는 함수
    def hash_value(self, key:Any)-> int:
        if isinstance(key, int):
            return key%self.capacity
        return(int(hashlib.sha256(str(key).encode().hexdigest(),16)%self.capacity))
    
    def search(self, key:Any)-> Any:
        hash = self.hash_value(key) #key에 해당하는 해시값
        p= self.table[hash] #해시테이블에서 그 해시값에 해당하는 노드?

        while p is not None:
            if p.key==key:#key값과 일치하는 노드를 찾으면
                return p.value #해당 노드의 값을 return
            p= p.next #뒤쪽 노드
            #p.next: p노드의 다음 노드를 가리키는 링크
        return None #일치하는 노드가 없으면 None을 반환
    
    def add(self, key: Any, value: Any)-> bool:

        hash = self.hash_value(key)
        p= self.table[hash]
        
        while p is not None:
            if p.key==key:#키와 같은 값이 발견되면 이미 있는 값이므로 
                return False #False 리턴하기!
            p=p.next #추가하려는 값과 일치하는 값을 가진 노드가 없으면 새로운 노드를 생성하여 연결리스트 맨 앞에 추가

        temp = Node(key, value, self.table[hash])
        self.table[hash] =temp
        return True
    
    def remove(self, key: Any) -> bool:
        #함수선언 구문
        '''
        -> : 함수의 반환 타입을 지정하는 주석
        remove 함수가 key라는 매개변수를 받고,
        bool타입의 값을 반환한다.
        self : remove를 호출하는 객체 자신을 나타내는 특별한 매개변수!
        key: Any 
        Any는 타입 힌트로 사용된것 . 모든 타입을 나타내는 
        특수한 타입힌트이다.
        '''
        hash= self.hash_value(key)
        p=self.table[hash]
        pp=None#이전 노드

        while p is not None:
            if p.key ==key:
                if pp is None:
                    #삭제할 노드가 연결리스트의 첫번째 노드인 경우
                    self.table[hash]= p.next
                else:
                    pp.next = p.next #12삭제할 노드를 다음 노드로 설정
                return True
            pp = p #현재 노드를 이전 노드로 설정
            p=p.next #
        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p= self.table[i]
            print(i, end=' ')
            while p is not None:
                print(f' -> {p.key}({p.value})', end ='')
                p= p.next
            print()

