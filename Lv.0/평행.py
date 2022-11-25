def solution(dots):
#     answer = 0
#     a = dots[0][0] - dots[1][0]
#     b = dots[0][1] - dots[1][1]
#     c = dots[2][0] - dots[3][0]
#     d = dots[2][1] - dots[3][1]
    
#     if (a/b == c/d) : return 1

#     a=dots[0][0]-dots[2][0]
#     b=dots[0][1]-dots[2][1]
#     c=dots[1][0]-dots[3][0]
#     d=dots[1][1]-dots[3][1]
    
#     if (a/b == c/d) : return 1

#     a=dots[0][0]-dots[3][0]
#     b=dots[0][1]-dots[3][1]
#     c=dots[1][0]-dots[2][0]
#     d=dots[1][1]-dots[2][1]
    
#     if (a/b == c/d) : return 1
#     return answer

#두 점의 y 좌표의 차를 x 좌표의 차로 나눈 것과 같다.
# y2 - y1 / x2 - x1

# def solution(dots):
#     [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
#     answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
#     answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
#     answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
#     return 1 if answer1 or answer2 or answer3 else 0

    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y2-y1)/(x2-x1) == (y4-y3)/(x4-x3))
    answer2 = ((y3-y1)/(x3-x1) == (y4-y2)/(x4-x2))
    answer3 = ((y4-y1)/(x4-x1) == (y3-y2)/(x3-x2))
    return 1 if answer1 or answer2 or answer3 else 0