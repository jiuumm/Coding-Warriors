def hanoi(원반개수, 시작, 목표, 보조):
    if 원반개수==1:
        print(시작, '->', 목표)
        return
    '''
    가장 큰 원반을 제외한 나머지 원반들을
    보조기둥이 목표기둥이 되고 목표기둥이 보조기둥이 되도록 한다.
    물론 시작기둥은 똑같다.
    '''
    #나머지 원반들 기준
    hanoi(원반개수-1, 시작, 보조, 목표)
    print(시작, '->', 목표)#가장 큰 원반기둥을 목표로
    #이제 나머지 원반들의 보조기둥이 시작기둥이 되고,목표기둥은 목표기둥,
    #시작 기둥은 보조기둥이 된다.(비교대상은 처음 애!)
    hanoi(원반개수-1, 보조, 목표, 시작)

hanoi(3,1,2,3)



def hanoi2(n, 시작, 목표, 보조):
    if n==1:
        print(시작,"->", 목표)
        return
    hanoi2(n-1, )