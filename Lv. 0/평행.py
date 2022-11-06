def solution(dots):
    c1 = abs(dots[0][1] - dots[1][1]) / abs(dots[0][0] - dots[1][0])
    c2 = abs(dots[2][1] - dots[3][1]) / abs(dots[2][0] - dots[3][0])
    c11 = abs(dots[0][1] - dots[2][1] / abs(dots[0][0] - dots[2][0]))
    c22 = abs(dots[1][1] - dots[3][1] / abs(dots[1][0] - dots[3][0]))
    c111 = abs(dots[0][1] - dots[3][1] / abs(dots[0][0] - dots[3][0]))
    c222 = abs(dots[1][1] - dots[2][1] / abs(dots[1][0] - dots[2][0]))
    if c1 == c2 or c11 == c22 or c111 == c222:
        return 1
    return 0