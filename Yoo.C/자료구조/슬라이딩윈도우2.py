import sys

input= sys.stdin.readline

S, P = map(int, input().split())
dna_lst = list(input()) #dna 문자열
tmp = list(map(int, input().split())) # 부분 문자열에 포함되어야 할 a,c,g,t, 의 최소 개수
tmp_dict = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
res_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
cnt=0


for i in range(S-P+1):# 왜 S-P+1인가?
    flag=True # 한번 다 돌고나면 다시 flag를 초기화 해줘야 함
    if i==0: #왜 i==0일때와 아닐 떄로 나눌까?-> 그래야 슬라이딩 윈도우를 구현할 수 있다.
        for j in range(P):
            res_dict[dna_lst[j]]+=1
    
    else:
        res_dict[dna_lst[i-1]]-=1
        res_dict[dna_lst[i+P-1]]+=1
    
    for j in {'A', 'C', 'G', 'T'}:
        
        if res_dict[j]<tmp_dict[j]:
            flag=False
            break

    if flag==True:
        cnt+=1
        
print(cnt)


        

        
        
