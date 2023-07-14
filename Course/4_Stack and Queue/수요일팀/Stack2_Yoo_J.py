#스택 프로그램 만들기

from enum import Enum
from Stack1_Yoo_J import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def selec_menu()-> Menu:
    s=[f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n=int(input(': '))
        if 1<=n<=len(Menu):
            return Menu(n)
        
s=FixedStack(64)

while True:
    print(f'현재 데이터 개수: {len(s)}/{s.capacity}')
    menu=selec_menu
    
    if menu==Menu.푸시:
        x=int(input("데이터를 입력하세요: "))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택 꽉참') 
    elif menu==Menu.팝:
        try:
            x=s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.empty:
            print("스택 비어있음")    
    elif menu==Menu.피크:
        try:
            x=s.peek
        except FixedStack.Empty:
            print("스택이 비어있음")
            
    elif menu==Menu.검색:
        x = int(input("검색할 값을 입력하세요: "))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print("검색한 값을 찾을 수 없습니다.")
    elif menu == Menu.덤프:
        s.dump()
        
    else:
        break            