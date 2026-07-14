# q7)Wap to find and display fibonacci series of N numbers using udf:

def fibbo(n):
    a = 0
    b = 1
    for i in range(0,n):
        print(a)
        c = a+b
        a = b
        b = c

n = int(input("enter the terms:"))
fibbo(n)
