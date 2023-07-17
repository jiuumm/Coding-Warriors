def hanoi(원반개수, 시작, 목표, 보조):
    if 원반개수==1:
        print(시작, '->', 목표)
        return
    hanoi(원반개수-1, 시작, 보조, 목표)
    print(시작, '->', 목표)
    hanoi(원반개수-1, 보조, 목표, 시작)

hanoi(3,1,2,3)