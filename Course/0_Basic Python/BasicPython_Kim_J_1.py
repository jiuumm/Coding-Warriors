# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:17:01 2023

@author: user
"""

# P.6078: 원하는 문자가 입력될 때까지 반복 출력하기

flag = True

while True:
    ch = input()    
    if flag == True:
        print(ch)
    if ch == 'q':
        flag = False
