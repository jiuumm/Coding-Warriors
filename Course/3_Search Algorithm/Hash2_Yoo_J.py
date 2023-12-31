#오픈주소법으로 해시함수 만들기
from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷-> 키, 값, 상태(stat)
class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1     # 비어 있음
    DELETED = 2   # 삭제 완료

class Bucket:

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성
    #속성 정하기
    def set_status(self, stat: Status) -> None:
        self.stat = stat

class OpenHash:
    

    def __init__(self, capacity: int) -> None:
      
        self.capacity = capacity                 # 해시 테이블 크기
        self.table = [Bucket()] * self.capacity  # 해시 테이블 만들기

    def hash_value(self, key: Any) -> int:
       
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)
    #재해시
    def rehash_value(self, key: Any) -> int:
        return(self.hash_value(key) + 1) % self.capacity

    #버킷 검색 함수
    def search_node(self, key: Any) -> Any:
        
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            #만약 해시값은 같은데 값이 다르면 재해시를 시작한다
            hash = self.rehash_value(hash)  
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        # search_node 메서드를 호출하여 일치하는 버킷 검색후 return
        # 편리하게 값 검색하기 위한 wrapper역할
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None     # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        # 이미 등록된 키
        if self.search(key) is not None:
            return False             
        #등록되지 않은 키라면?
        hash = self.hash_value(key)  
        p = self.table[hash]         # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  
            p = self.table[hash]
        return False                      

    def remove(self, key: Any) -> int:
       
        p = self.search_node(key)  # 버킷을 주목
        if p is None:
            return False           # 이 키는 등록되어 있지 않음
        #해당 값 지우기
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:

        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- 삭제 완료 --')