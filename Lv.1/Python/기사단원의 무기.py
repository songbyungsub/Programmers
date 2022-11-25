def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    divisorsList.sort()
    return divisorsList

def solution(number, limit, power):
    answer = 0
    count = []
    for i in range(1,number+1):
        count.append(len(getMyDivisor(i)))
    for i in count:
        if i > limit:
            i = power
        answer += i
    return answer