
'''
배열 vs 리스트

1. 리스트
- 리스트의 아이템들을 대괄호로 묶인다.
- 정렬 돼 있다
- 변경 가능
- 중복 가능
- 여러가지 데이터 타입이 가능(같은 리스트에 object, string, integer)

2. 배열
- 대괄호, 정렬, 변경, 중복 모두 가능
- 어떤 배열의 종류를 사용하냐에 따라 여러가지 데이터 타입이 가능할
수도, 아닐 수도 있음.
-선언 되어야 함


'''
a= [10,20,30]
max=a[0]
if a[1]>max: max=a[1]
if a[2]>max: max=a[2]

print(max)

def max_of(a):
    max=a[0]
    for i in range(1, len(a)):
        if a[i]>max:
            max=a[i]
    return max
            
print(max_of(a))
    

