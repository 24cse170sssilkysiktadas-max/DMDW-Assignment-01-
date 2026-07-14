# Q6)wap to test a number is prime or not using udf.

def Prime(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count = count+1
    if(count==2):
        print("it is prime number")
    else:
        print("it is not prime")

n = int(input("enter the number"))
Prime(n)
