#230718 TUE
#05-3 하노이의 탑
#실습 5-6

def move(no: int, x: int, y: int) -> None:
    '''원반 no개를 x기둥에서 y기둥으로 옮김'''
    if no>1:
        move(no -1, x, 6-x-y)

    print(f'원반 [{no}]을 {x}기둥에서 {y}기둥으로 옮깁니다')

    if no>1:
        move(no-1,6-x-y,y)

print('하노이의 탑을 구현합니다')
n= int(input('원반의 개수를 입력하세요: '))

move(n,1,3) #1기둥에 쌓인 원반 n개를 3기둥으로 옮김

#05-4 8퀸 문제
#실습 5-7

#각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0]*8         #각 열에서 퀸의 위치를 출력

def put() -> None:
    '''각 열에 배치한 퀸의 위치를 출력'''
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i:int) -> None:
    '''i열에 퀸을 배치'''
    for j in range(8):
        pos[i] = j      #퀸을 j행에 배치
        if i==7:        #모든 열에 퀸 배치를 종료
            put()
        else:
            set(i+1)    #다음 열에 퀸을 배치

set(0)      #0열에 퀸 배치

#실습 5-8

#행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos=[0] *8      #각 열에서 퀸의 위치
flag = [False ] *8      #각 행에 퀸을 배치했는지 체크

def put() -> None:
    '''각 열에 배치한 퀸의 위치를 출력'''
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i:int) -> None:
    '''i열에 알맞은 위치에 퀸을 배치'''
    for j in range(8):
        if not flag[i]:         #j행에 퀸을 배치하지 않았으면
            pos[i] = j          #퀸을 j행에 배치
            if i==7:            #모든 열에 퀸 배치를 완료
                put()
            else:
                flag[j] = True
                set[i+1]        #다음 열에 퀸을 배치
                flag[j] = False

set(0)                          #0열에 퀸을 배치

#실습 5-9

#8퀸 문제 알고리즘 구현하기

pos = [0] *8            #각 열에 배치한 퀸의 위치
flag_a = [False] *8     #각 행에 퀸을 배치했는지 체크
flag_b = [False] *15    #대각선 방향으로 퀸을 배치했는지 체크
flag_c = [False] *15    #대각선 방향으로 퀸을 배치했는지 체크

def put() -> None:
    '''각 열에 배치한 퀸의 위치 출력'''
    for i in range(8):
        print(f'pos[i]:2', end='')
    print()

def set(i: int) -> None:
    '''i열의 알맞은 위치에 퀸을 배치'''
    for j in ragne(8):
        if(    not flag_a[j]
        and not flag_b[i+1]
        and not flag_c[i=j+7]):
            pos[i] = j
            if i==7:
                put()
            else:
                flag_a=flag_b[i+j]=flag_c[i-j+7]=True
                set(i+1)
                flag_a[j] = flag_b[i+j]=flag_c[i-j+7]=False

    set(0)      #0열에 퀸을 배치

