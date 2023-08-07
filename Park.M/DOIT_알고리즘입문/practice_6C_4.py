#sorted()함수를 사용하여 정렬하기

print('sorted()함수를 사용하여 정렬합니다.')
num = int(input('원소 수를 입력하세요: '))
x = [None] *num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))                         #배열 x의 값들 입력

x = sorted(x)                                              #배열 x를 오름차순으로 정렬
print('오름차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')

x = sorted(x, reverse=True)                                #배열 x를 내림차순으로 정렬
print('내림차순으로 정렬했습니다.')
for i in range(num):
    print(F'x[{i}] = {x[i]}')