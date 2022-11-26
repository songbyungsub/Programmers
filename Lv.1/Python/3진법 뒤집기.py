def solution(n):
    answer = 0
    a = ''
    while(n):
        a += str(n%3)   
        n //= 3
    
    answer = int(a,3)
    return answer