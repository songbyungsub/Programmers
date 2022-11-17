def solution(str1, str2):
    answer = 2
    for i in str1:
        if str2 in str1:
            answer = 1
    return answer