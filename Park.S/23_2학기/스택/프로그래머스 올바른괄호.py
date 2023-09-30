#230916(SAT) / 스택 / 프로 올바른괄호(Lv.2)
'''
( 를 만날 때마다 stack에 push한다. 계속 쌓이다가 ) 를 만나면 ( 을 pop 한다.
1. 그러다가 stack이 비면 true.
2. 비어있는 stack에 괄호가 남아있으면 false. 
3. 처음에  ) 괄호가 먼저 나올 때도 false.
'''


def solution(s):
    stack = [] 

    for char in s:
        if char == '(':         # 열린 괄호면 stack에 push
            stack.append(char)
        else:                   # 닫힌 괄호면 스택에서 짝지어진 열린 괄호 pop
            if not stack:       # 스택이 비어있으면 false
                return False
            stack.pop()

    #스택에 남은 괄호가 없어야 true
    return len(stack) == 0
