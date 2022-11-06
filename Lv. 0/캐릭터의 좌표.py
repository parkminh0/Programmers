def solution(keyinput, board):
    result = [0, 0]
    for i in keyinput:
        if i == 'left':
            if abs(result[0]-1) >= board[0]/2:
                continue
            result[0] -= 1
        elif i == 'right':
            if abs(result[0]+1) >= board[0]/2:
                continue
            result[0] += 1
        elif i == 'up':
            if abs(result[1]+1) >= board[1]/2:
                continue
            result[1] += 1
        else:
            if abs(result[1]-1) >= board[1]/2:
                continue
            result[1] -= 1
    return result