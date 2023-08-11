#230720 THUR
#08-3 커서를 이용한 연결리스트

#실습 8-3
#커서로 연결리스트 구현

from __future__ import annotations
from typing import Any,Type

Null = -1

class Node:
    '''연결리스트용 노드클래스(배열커서 버전)'''

    def __init__(self, data=Null, next=Null, dnext = Null):
        '''초기화'''
        self.data = data
        self.next = next
        self.dnext = dnext

class ArrayLinkedList:
    '''연결리스트 클래스(배열커서 버전)'''

    def __init__(self,capacity:int):
        '''초기화'''
        self.head = Null
        self.current = Null
        self.max= Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no =0

    def __len(self) -> int:
        '''연결리스트의 노드수 반환'''
        return self.no

    def get_insert_index(self):
        '''다음에 삽입할 레코드의 인덱스 구함'''
        if self.deleted == Null:
            if self.max +1 < self.capacity:
                self.max +=1
                return self.max
            else:
                return Null
        else:
            rec= self.deleted
            self.deleted = self.n[rec].dnext    #프리 리스트에서 맨앞rec 꺼내기
            return rec

    def delete_index(self, idx:int)-> None:
        '''레코드 idx를 프리리스트에 등록'''
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec=self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    def search(self,data:Any) -> int:
        '''data와 값이 같은 노드 검색'''
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data ==data:
                self.current=ptr
                return cnt
            cnt +=1
            ptr = self.n[ptr].next
        return Null

    def __contains__(self, data:Any) ->bool:
        '''연결리스트에 data 포함돼있는지 확인'''
        return self.search(data) >=0

    def add_first(self,data:Any):
        '''머리노드에 삽입'''
        ptr = self.head
        rec = self.get_insert_index()
        if rec!= Null:
            self.head = self.current = rec
            self.n[self.head] = Node[data,ptr]
            self.no +=1

    def add_last(self,data:Any) -> None:
        '''꼬리노드에 삽입'''
        if self.head ==Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr= self.n[ptr].next
            rec=self.get_insert_index()

            if rec!=Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no +=1

    def remove_first(self) -> None:
        '''머리노드 삭제'''
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -=1

    def remove_last(self) -> None:
        '''꼬리노드 삭제'''
        if self.head != Null:
            if self.n[self.head].next ==Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next!=Null:
                    pre =ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null
                self.delete_index(ptr)
                self.current = pre
                self.no -=1

    def remove(self,p:int) -> None:
        '''레코드 p 삭제'''
        if self.head!=Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return
                self.n[ptr].next=Null
                self.delete_index(p)
                self.n[ptr].next=self.n[p].next
                self.current=ptr
                self.no -=1

    def remove_current_node(self) -> None:
        '''주목노드를 삭제'''
        self.remove(self.current)

    def clear(self) -> None:
        '''모든 노드 삭제'''
        while self.head !=Null:
            self.remove_first()
        self.current= Null

    def nex(self) ->bool:
        '''주목노드를 한칸 뒤로 이동'''
        if self.current = Null or self.n[self.current].next ==Null:
            return False        #이동할 수 x
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) ->None:
        '주목노드를 출력'
        if self.current == Null:
            print('주목 노드가 없습니다')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        '''모든노드 출력'''
        ptr = self.head

        while ptr!=Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) ->None:
        '''배열을 덤프'''
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        '''이터레이터 반환'''
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:

    def __init(self,n:int,head:int):
        self.n= n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current ==Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data

#08-4 원형 이중 연결리스트

from __future__ import annotations
from typing import Any,Type

class Node:
    '''원형 이중연결 리스트용 노드 클래스'''

    def __init__(self, data:Any = None, prev: Node = None,
                 next: Node = None) -> None:
        '''초기화'''
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    '''원형 이중연결 리스트 클래스'''

    def __init(self) -> None:
        '''초기화'''
        self.head = self.current = Node()
        self.no=0

    def  __init__(self) -> None:
        self.head = self.current= Node()
        self.no=0

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        '''리스트가 비었는지 확인'''
        return self.head.next is self.head

    def __contains__(self, data:Any) -> bool:
        '''data와 값 같은 노드 검색'''
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt +=1
            ptr = ptr.next
        return -1           #검색 실패

    def __contains__(self,data:Any) -> bool:
        '''연결리스트에 data 포함됐는지 판단'''
        return self.search(data) >=0

    def print_current_node(self) -> None:
        '''주목 노드 출력'''
        if self.is_empty():
            print('주목 노드는 없습니다')
        else:
            print(self.current.data)

    def print(self) -> None:
        '''모든 노드 출력'''
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        '''모든 노드를 역순으로 출력'''
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        '''주목 노드를 한칸 뒤로 이동'''
        if self.is_empty() or self.current.next is self.head:
            return False        #이동불가
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        '''주목 노드 한칸 앞으로 이동'''
        if self.is_empty() or self.current.prev is self.head:
            return False  #이동불가
        self.current = self.current.prev
        return True

    def add(self,data:Any) -> None:
        '''주목노드 바루 뒤에 노드삽입'''
        node = Node(data,self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no +=1

    def add_first(self,data : Any) -> None:
        '''맨앞에 노드 삽입'''
        self.current = self.head
        self.add(data)

    def add_last(self,data:Any) -> None:
        '''맨뒤에 노드 삽입'''
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self) -> None:
        '''주목 노드 삭제'''
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self,p: Node) -> Node:
        '''노드p삭제'''
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:        #p 발견
                self.current = p
                self.remove_current_node()
                break
            ptr=ptr.next

    def remove_first(self) -> None:
        '''머리 노드 삭제'''
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        '''꼬리 노드 삭제'''
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self) -> None:
        '''모든 노드 삭제'''
        while not self.is_empty():
            self.remove_first()
        self.no = 0

    def __iter__(self) -> DoubleLinkedListIterator:
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        '''내림차순 이터레이터 반환'''
        return DoubleLinkedListReverseIterator(self.head)

    class DoubleLinkedListIterator:

        def __init__(self,head:None):
            self.head=head
            self.current=head.next

        def __iter__(self) -> DoubleLinkedListIterator:
            return self

        def __next__(self) -> Any:
            if self.current is self.head:
                raise StopIteration
            else:
                data = self.current.data
                self.current = self.current.next
                return data

    class DoubleLinkedListReverseIterator:
        '''내림차순 이터레이터 클래스'''
        def __init__(self,head:Node):
            self.head = head
            self.current = head.prev

        def __iter__(self) -> DoubleLinkedListReverseIterator:
            return self

        def __next__(self) -> Any:
            if self.current is self.head:
                raise StopIteration
            else:
                data = self.current.data
                self.current = self.current.prev
                return data


