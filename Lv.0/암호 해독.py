def solution(cipher, code):
    #answer = ''
    # for i in range(int(code)-1,len(cipher),int(code)):
    #     answer += cipher[i]
    answer = cipher[code-1::code]
    return answer