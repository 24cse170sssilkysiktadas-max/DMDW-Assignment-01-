# wap to create a udf for finding the greatest among 3 numbers:

def greatest(a,b,c):
    if a>b and a>c :
        print(a,"is greatest")
    elif b>a and b>c :
        print(b,"is gratest")
    else:
        print(c,"is gratest")


a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))
greatest(a,b,c)
