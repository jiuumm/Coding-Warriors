import sys
sys.stdin = open("in2.txt", "rt")
N= int(input())
score = list(map(int, input().split()))

avr=0
sum=0
for i in range(len(score)):
    sum+=score[i]
    
#전체 학생 평균(소수 첫번째 자리에서 반올림)

avr = round(sum/N)

for i in range(len(score)):
    if score[i]-avr>=0:
        score[i]= score[i]-avr
    else:
        score[i]= avr-score[i]
print(score)
lst=[]    
min= score[0]    
for i in range(1,len(score)):
    
    if min>=score[i]:
        min=score[i]
        lst.append(i+1)
        

    

        

print(lst)

