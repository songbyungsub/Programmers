def solution(id_pw, db):
    answer = 'fail'
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                answer = 'login'
            elif id_pw[1] != i[1]:
                answer = 'wrong pw'
    return answer