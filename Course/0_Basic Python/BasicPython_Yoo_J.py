#코드업 1283번
a = int(input())
b = int(input())
dayList = list(map(int, input().split()))
result=0
temp=a
for i in dayList:   
    temp *= (1+i*0.01)
   
result = round(temp-a)
print(result)

if result<0:
    print("bad")
elif result>0:
    print("good")
else:
    print("same")
