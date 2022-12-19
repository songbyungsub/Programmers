def prime(n):
    count = 0
    for i in range(2,n):
        if n % i == 0:
            count += 1
    return count

def solution(n):
    answer = []
    for i in range(1, n+1):
        answer.append(prime(i))
    return answer