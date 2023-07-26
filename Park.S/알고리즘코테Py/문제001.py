#230726(WED)
#001. 숫자의 합 구하기 (백준 브론즈4 11720번)

N = input()        # 아래 nums의 원소들을 int형으로 바꾸기 때문에 굳이 N에서 int(input())으로 할 필요x
nums = list(input())    #Python에서 리스트는 배열의 특징까지 모두 가짐
sum = 0                 #더하기 연산 할 저장공간 필요 / 변수 선언

for i in nums:
    sum += int(i)       #nums 내의 각 숫자들 가져와서 sum 변수에 더하기

print(sum)              #출력