def solution(n, t):
    answer = 0
    while t > 0:
        n *= 2
        t -= 1
    return n