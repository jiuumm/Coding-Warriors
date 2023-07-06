board = []

# 20x20 크기의 보드 생성
for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

# 보드에 값을 입력받음
for i in range(19):
    a = input().split()
    for j in range(19):
        board[i + 1][j + 1] = int(a[j])

# 뒤집을 횟수 입력받음
n = int(input())

# 뒤집기 연산 수행
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    # 해당 열의 값을 뒤집음
    for j in range(1, 20):
        if board[j][y] == 0:
            board[j][y] = 1
        else:
            board[j][y] = 0

    # 해당 행의 값을 뒤집음
    for j in range(1, 20):
        if board[x][j] == 0:
            board[x][j] = 1
        else:
            board[x][j] = 0

# 보드 출력
for i in range(1, 20):
    for j in range(1, 20):
        print(board[i][j], end=' ')
    print()

