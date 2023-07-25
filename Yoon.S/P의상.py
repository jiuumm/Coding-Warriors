def solution(clothes):
    answer = 1 # 기본 한 개
    closet = {cloth[1]: [] for cloth in clothes} # 의상의 종류를 key로 한 딕셔너리 closet 생성
    
    for cloth in clothes:
        closet[cloth[1]].append(cloth[0]) # key에 맞게 value 할당
    
    for clothes_types in closet.keys():
        num = len(closet[clothes_types]) # key 별 value 개수 num
        answer *= (num + 1) # num + 해당 종류에서 아무것도 입지 않을 때
    
    return answer - 1 # 무엇이든 하나는 입어야 하므로, 아무것도 안 입는 경우 제거
