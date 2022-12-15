def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    bad = [3,2,1]
    good = [5,6,7]
    
    for i in range(len(survey)):
        if choices[i] in bad:
            dic[survey[i][0]] += bad.index(choices[i])+1
        elif choices[i] in good:
            dic[survey[i][1]] += good.index(choices[i])+1
            
    arr = [['R','T'],['C','F'],['J','M'],['A','N']]
    
    for i in arr:
        if dic[i[0]] >= dic[i[1]]:
            answer += i[0]
        else: answer += i[1]
    return answer