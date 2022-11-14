def solution(board, moves):
    answer = 0
    tmp = [0]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if tmp[-1] == board[j][i-1]:
                    board[j][i-1] = 0
                    tmp.pop()
                    answer += 2
                    break
                else:
                    tmp.append(board[j][i-1])
                    board[j][i-1] = 0
                    break    

    return answer