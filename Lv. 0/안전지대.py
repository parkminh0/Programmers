def solution(board):
    answer = 0
    tmp = []
    
    for i in range(len(board)+2):
        push = []
        for j in range(len(board)+2):
            push.append(0)
        tmp.append(push)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                tmp[i][j] = 1
                tmp[i][j+1] = 1
                tmp[i][j+2] = 1
                tmp[i+1][j] = 1
                tmp[i+1][j+1] = 1
                tmp[i+1][j+2] = 1
                tmp[i+2][j] = 1
                tmp[i+2][j+1] = 1
                tmp[i+2][j+2] = 1

    for i in range(1, len(tmp)-1):
        for j in range(1, len(tmp)-1):
            if tmp[i][j] == 0:
                answer += 1
    return answer
    