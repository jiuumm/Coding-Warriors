m = []

# 12x12 크기의 맵 생성
for i in range(12):
    m.append([])
    for j in range(12):
        m[i].append(0)

# 맵에 값을 입력받음
for i in range(10):
    a = input().split()
    for j in range(10):
        m[i + 1][j + 1] = int(a[j])

x = 2
y = 2

# 탐색 시작
while True:
    if m[x][y] == 0:
        m[x][y] = 9
    elif m[x][y] == 2:
        m[x][y] = 9
        break

    # 더 이상 진행할 수 없는 경우
    if (m[x][y + 1] == 1 and m[x + 1][y] == 1) or (x == 9 and y == 9):
        break

    # 오른쪽으로 이동할 수 있으면 이동
    if m[x][y + 1] != 1:
        y += 1
    # 오른쪽으로 이동할 수 없으면 아래로 이동
    elif m[x + 1][y] != 1:
        x += 1

# 맵 출력
for i in range(1, 11):
    for j in range(1, 11):
        print(m[i][j], space=' ')
    print()
