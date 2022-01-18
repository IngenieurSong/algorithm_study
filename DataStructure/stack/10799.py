board = list(input())
answer = 0
stack = []

for i in range(len(board)):
    if board[i] == "(":
        stack.append('(')
        
    else:
        if board[i - 1] == "(":
            stack.pop()
            answer += len(stack)
            
        else:
            stack.pop() 
            answer += 1

print(answer)
