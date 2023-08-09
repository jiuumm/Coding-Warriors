#커서로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """연결 리스트용 노드 클래스(배열 커서 버전)"""

    def __init__(self, data=Null, next=Null, dnext=Null):
        """초기화"""
        self.data = data                                        #데이터
        self.next = next                                        #리스트 뒤쪽 포인터
        self.dnext = dnext                                      #프리 리스트의 뒤쪽 포인터


class ArrayLinkedList:
    """연결 리스트 클래스(배열 커서 버전)"""

    def __init__(self, capacity: int):
        """초기화"""
        self.head = Null                                        #머리노드
        self.current = Null                                     #주목노드
        self.max = Null                                         #사용중인 꼬리 레코드
        self.deleted = Null                                     #프리 리스트의 머리 노드
        self.capacity = capacity                                #리스트의 크기
        self.n = [Node()] * self.capacity                       #리스트 본체
        self.no = 0                                             #리스트의 노드 수....?

    def __len__(self) -> int:
        """연결 리스트의 노드 수를 반환"""
        return self.no
    
    def get_insert_index(self):
        """다음에 삽입할 레코드의 인덱스를 구함"""
        if self.deleted == Null:                                #삭제 레코드는 존재하지 않음
            if self.max+1 < self.capacity:
                self.max += 1
                return self.max                                 #새 레코드를 사용
            else:
                return Null                                     #크기 초과
        else:
            rec = self.deleted
            self.deleted self.n[rec].dnext                      #프리 리스트에서 맨 앞 rec를 꺼내기
            return rec
    
    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted == Null:                                #삭제 레코드는 존재하지 않음
            self.deleted = idx
            self.n[idx].dnext = Null                            #idx를 프리 리스트의 맨 앞에 등록
        else:
            rec = self.deleted  
            self.deleted = idx                                  #idx를 프리 리스트의 맨 앞에 삽입
            self.n[idx].dnext = rec
    
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""4
        cnt = 0
        ptr = self.head                                         #현재 스캔 중인 노드
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr 
                return cnt                                      #검색 성공
            cnt += 1
            ptr = self.n[ptr].next                              #뒤쪽 노드에 주목
        return Null                                             #검색 실패
    
    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0
    
    def add_first(self, data: Any):
        """머리 노드에 삽입"""
        ptr = self.head
        rec = self.get_insert_index()
        if rec!=Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec!=Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head!= Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1
    
    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        