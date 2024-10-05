def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

m = int(input("1번째 숫자: "))
k = input("수식: ")

if (k != '+' and k != '-'):
    print("수식 없음")
    exit()
    
n = int(input("2번째 숫자: "))
        

if(k == '+'):
    print("결과:", add(m,n))
    
elif(k == '-'):
    print("결과:", subtract(m,n))


    
