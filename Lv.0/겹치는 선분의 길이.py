def solution(lines):
    answer = []
    new=[]
    a = lines[0]
    b = lines[1]
    c = lines[2]
    a_l =[]
    b_l =[]
    c_l =[]
    for i in range(a[0],a[1]):
        a_l.append(i)
    for i in range(b[0],b[1]):
        b_l.append(i)
    for i in range(c[0],c[1]):
        c_l.append(i)
    total = a_l + b_l + c_l
    
    for i in total:
        if i not in new:
            new.append(i)
        else:
            if i not in answer:
                answer.append(i)
        
    return len(answer)