def solution(n):
    answer = ''
    while n > 0:
        answer += '수'
        n -=1
        if n == 0:
            break
        answer +='박'
        n -=1
    return answer