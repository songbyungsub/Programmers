def solution(strings, n):
    trings=sorted(strings, key=lambda x:(x[n],x[0:]))
    return trings