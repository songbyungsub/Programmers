def solution(n):
    answer = 2
    for i in range(1000001):
        if n == i*i:
            answer = 1
    return answer