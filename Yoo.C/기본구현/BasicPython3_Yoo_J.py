#코드업 기본 100제 1172번

a,b,c =map(int, input().split())
lst=[a,b,c]
lst.sort()
for i in range(len(lst)):
    print(lst[i], end=' ')
    
   
# 코드업 기본 100제 1420번
#딕셔너리 이용!
n = int(input())
dit = {}
for i in range(n):
    name, score = input().split()
    dit[name]= int(score)

#내림 차순으로 정리하기 위해 reverse=True로 바꿔주기    
answer = sorted(dit.items(), key= lambda x:x[1], reverse=True)
print(answer[2][0])

    
    

    
    