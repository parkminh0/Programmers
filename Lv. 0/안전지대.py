def solution(board):
    answer = 0
    tmp = []
    for i in range(len(board)+2):
        tmp.append(0)
    
    for j in board:
        j.insert(0, 0)
        j.append(0)
    
    board.insert(0,tmp)
    board.append(tmp)
    
    tmp = []
    for k in range(1, len(board)-1):
        for l in range(1, len(board)-1):
            if board[k][l] == 1:
                tmp.append([k, l])
                
    for m in tmp:
        board[m[0]-1][m[1]-1] = 1
        board[m[0]-1][m[1]] = 1
        board[m[0]-1][m[1]+1] = 1
        board[m[0]][m[1]-1] = 1
        board[m[0]][m[1]+1] = 1
        board[m[0]+1][m[1]-1] = 1
        board[m[0]+1][m[1]] = 1
        board[m[0]+1][m[1]+1] = 1
    
    cnt = 0
    for x in range(1, len(board)-1):
        for y in range(1, len(board)-1):
            cnt += 1
            if board[x][y] == 1:
                answer += 1
    return cnt-answer