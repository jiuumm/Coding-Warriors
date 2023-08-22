#처음 내 코드..-> 너무 복잡 
N= int(input())
word=[]
for i in range(N):
    tmp = input()
    tmp=tmp.lower()
    word.append(tmp)


#k는 배열 안에 있는 문자열
def check(k):
    
    if k==k[::-1]:

        return True
    else:
        return False
        


for i in range(N):
    if check(word[i])==True:
        print("#",i+1, sep='', end=' ')
        print("YES")
    else:
        print("#",i+1, sep='', end=' ' )
        print("NO")



        
        