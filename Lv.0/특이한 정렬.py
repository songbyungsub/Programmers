def solution(numlist, n):
    answer = []
    if n in numlist:
        answer.append(n)
    for i in range(1,10000):
        if n+i in numlist:
            answer.append(n+i)
        if n-i in numlist:
            answer.append(n-i)
    return answer