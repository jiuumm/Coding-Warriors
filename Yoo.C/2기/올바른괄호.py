def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        
        if s[i]=='(':
            stack.append('(')
        
        #처음에 stack[-1]이 아니고 s[i-1]해서 계속 안나왔었다.
        elif s[i]==')'and stack and stack[-1]=='(' :
            stack.pop()
            
        elif not stack and s[i]==')':
            stack.append(")")
            
            
    if len(stack) !=0:
        answer = False
    else:
        answer = True
        
    return answer