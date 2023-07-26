#230720 THUR

#09-1 트리구조
#주요 용어들!

#09-2 이진 트리와 이진검색 트리

#실습 9-1
#이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any,Type

class Node:
    '''이진검색 트리의 노드'''
    def __init__(self,key:Any, value:Any, left:Node = None,
                 right:Node = None):
        '''생성자'''
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    '''이진 검색 트리'''

    def __init(self):
        '''초기화'''
        self.root = None

    def search(self,key:Any) -> Any:
        '''키가 key인 노드 검색'''
        p = self.root       #루트에 주목
        while True:
            if p is None:        #더이상 진행할수 없으면
                return None      #검색 실패
            if key == p.key:     #key와 노드p의 키가 같으면
                return p.value   #검색 성공
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self,key : Any, value:Any) -> bool:
        '''키가 key이고 값이 value인 노드를 삽입'''

        def add_node(node: Node, key:Any, value: Any)-> None:
            '''node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입'''
            if key == node.key:
                return False    #key가 이진 검색 트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None,None)
                else:
                    add_node(node.right,key,value)
            return True

        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key, value)

    def remove(self, key:Any) -> bool:
        '''키가 key인 노드를 삭제'''
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                if key< p.key:
                    if_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left

        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self) -> None:
        '''덤프(모든 노드를 키의 오름차순으로 출력)'''

        def print_subtree(node:Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        print_subtree(self.root)

    def min_key(self) -> Any:
        '''가장 작은 키'''
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        '''가장 큰 키'''
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key

#실습 9-2
#이진검색 트리 클래스 BinarySearchTree 사용하기

from enum import Enum
#실습 9-1파일 import

Menu = Enum('Menu',['삽입','삭제','검색','덤프','키의범위','종료'])

def select_Menu() -> Menu:
    '''메뉴 선택'''
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end='')
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()       #이진검색 트리 생성

while Ture:
    menu = select_Menu()        #메뉴 선택

    if menu==Menu.삽입:          #삽입
        key = int(input('삽입할 키를 입력하세요: '))
        val = input('삽입할 키를 입력하세요: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요: '))
        tree.remove(key)

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다')
        else:
            print('해당하는 데이터가 없습니다')

    elif menu == Menu.덤프:
        tree.dump()

    elif menu == Menu.키의범위:
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최솟값은 {tree.max_key()}입니다.')

    else:
        break

