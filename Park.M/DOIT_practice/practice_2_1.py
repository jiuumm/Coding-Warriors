# 학생 5명의 시험점수를 입력받아 합계와 평균을 출력하기

print('학생 그룹의 점수의 합계와 평균을 구합니다.')

score_1 = int(input('학생 1의 점수를 입력하시오: '))
score_2 = int(input('학생 2의 점수를 입력하시오: '))
score_3 = int(input('학생 3의 점수를 입력하시오: '))
score_4 = int(input('학생 4의 점수를 입력하시오: '))
score_5 = int(input('학생 5의 점수를 입력하시오: '))

total=0
total += score_1
total += score_2
total += score_3
total += score_4
total += score_5

print(f'합계는 {total}입니다.')
print(f'평균은 {total/5}입니다.')