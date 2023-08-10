#그리디 알고리즘
#가장 큰 것부터!!

N= int(input())

lst=[]

for i in range(N):
    quo=0
    if (N-5*i) % 3 != 0 and (N-5*i)>=0:
        continue
    elif (N-5*i) %3 ==0 and (N-5*i)>=0:
        quo+= i
        tmp = (N-5*i)//3
        quo += tmp
        
        lst.append(quo)

if len(lst)==0:
    print(-1)
else:
    min= lst[0]
    for i in range(len(lst)):
        if min> lst[i]:
            min= lst[i]

    print(min)
    
     

