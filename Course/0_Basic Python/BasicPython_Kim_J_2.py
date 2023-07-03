# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 08:51:54 2023

@author: user
"""

# P.6098: 성실한 개미

m = []
for i in range(10):
    m.append(input().split())

x = 1
y = 1
m[x][y] = 9

while True:
    if m[x][y+1] == '0': 
        # 오른쪽 이동
        m[x][y+1] = 9
        y = y+1
    elif (m[x][y+1] == '1') & (m[x+1][y] == '0'): 
        # 아래로 이동
        m[x+1][y] = 9
        x = x+1
    elif m[x][y+1] == '2':
        # 오른쪽 먹이 발견
        m[x][y+1] = 9
        break
    elif m[x+1][y] == '2':
        # 아래쪽 먹이 발견
        m[x+1][y] = 9
        break  
    else:
        # 둘다 막힘
        break

for i in range(10):
    for j in range(10):
        print(m[i][j], end=' ')
    print()