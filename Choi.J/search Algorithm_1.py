#프로그래머스 해시-의상문제 코드 부연

"""
for cloth, category in clothes:
     
clothes 리스트의 각 요소를 순회하면서 각 요소를 cloth와 category로 언패킹하는 것.
clothes 리스트는 2차원 리스트로, 각 요소는 [의상의 이름, 의상의 종류]와 같은 형태.
예를 들어, clothes 리스트가 
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
일 때, 첫 번째 요소인 ["yellow_hat", "headgear"]를 cloth와 category로 언패킹. 
이때 cloth에는 "yellow_hat"이, category에는 "headgear"가 할당. -> 이후의 코드에서 cloth와 category 변수를 사용하여 작업을 수행.
"""

# sol2
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


#sol3
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
