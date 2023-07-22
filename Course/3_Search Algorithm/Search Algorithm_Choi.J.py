#프로그래머스 의상문제

def solution(clothes):
    # 의상 종류별 개수를 세기 위한 딕셔너리 초기화
    clothes_dict = {}

    # 의상 종류별 개수 세기
    for cloth, category in clothes:
        if category in clothes_dict:
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 1

    # 각 종류별 의상 개수에 1을 더한 값을 곱해줌
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)

    # 모든 종류의 의상을 선택하지 않는 경우 빼줌
    return answer - 1