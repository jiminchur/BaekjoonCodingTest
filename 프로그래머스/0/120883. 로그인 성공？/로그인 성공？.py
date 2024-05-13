def solution(id_pw, db):
    login_dic = {}
    for i in db:
        login_dic[i[0]] = i[1]
    try :
        if login_dic[id_pw[0]] == id_pw[1]:
            answer = "login"
        else :
            answer = "wrong pw"
    except :
        answer = "fail"
    return answer