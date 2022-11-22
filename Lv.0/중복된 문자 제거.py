def solution(my_string):
    answer = list(dict.fromkeys(my_string))
    return ''.join(answer)