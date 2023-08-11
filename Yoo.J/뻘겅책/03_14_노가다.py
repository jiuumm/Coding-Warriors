n= int(input()) #연산 횟수 
myQueue = []


def find(lst):
    tmpLst=[0]*len(lst)
    if len(lst) !=0:
        #리스트의 모든 값들 절댓값 씌우기
        for i in range(len(lst)):
            tmpLst[i]= abs(lst[i])
        
        min_abs = tmpLst[0]
        for i in range(len(lst)):
            if tmpLst[i]<min_abs:
                min_abs=tmpLst[i]
                
        min_tmp=[] #절댓값이 최소인 요소들의 인덱스 집합
        
        for j in range(len(lst)):
            if tmpLst[j]==min_abs:
                min_tmp.append(j)
        
        min = lst[min_tmp[0]]        
        realIdx = min_tmp[0]
        for i in min_tmp:
            if lst[i]<min:
                min=lst[i]
                realIdx= i
        print(lst[i])
        lst.pop(i)
            
                
                
            
                    
    else:
        print(0)        

for _ in range(n):
    num = int(input())
    if num != 0 :
        myQueue.append(num)
    else: #num이 0일 때
        find(myQueue)    
        

      

