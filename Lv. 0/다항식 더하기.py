def solution(polynomial):
    tmp = polynomial.split()
    t = ''
    x = 0
    y = 0
    for i in tmp:
        if i.isdigit() == True:
            y += int(i)
        elif i == '+':
            continue
        elif i == 'x':
            x += 1
        else:
            for j in i:
                if j.isdigit() == True:
                    t += str(j)
            x += int(t)
            t = ''
    if x == 0:
        return str(y)
    elif y == 0:
        if x == 1:
            return 'x'
        return str(x) + 'x'
    elif x == 1:
        return 'x + ' + str(y)
    else:
        return str(x) + 'x + ' + str(y)