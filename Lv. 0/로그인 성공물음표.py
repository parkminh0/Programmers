def solution(id_pw, db):
    result = 'fail'
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] != id_pw[1]:
                result = 'wrong pw'
            else:
                result = 'login'
    return result