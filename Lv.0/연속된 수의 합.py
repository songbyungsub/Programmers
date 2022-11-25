def solution(num, total):
    answer = []
    c = total // num
    #홀수
    if num % 2 == 1:
        for i in range(c-num//2, c+num//2+1):
            answer.append(i)
    else:
          for i in range(c-num//2+1, c+num//2+1):
                answer.append(i)
    return answer