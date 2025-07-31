# fibonacci 1 1 2 3 5 8 13 21 34 55

def fib(n):
    if n<=1:
       return n
    else:
        return fib(n-1)+fib(n-2)
num=int(input("enter terms:"))
for i in range(num):
    print(fib(i),end=' ')
# fibonacci 1 1 2 3 5 8 13 21 34 55

def fib(n):
    if n<=1:
       return n
    else:
        return fib(n-1)+fib(n-2)
num=int(input("enter terms:"))
for i in range(num):
    print(fib(i),end=' ')


def dsum(n):
    if n==0:
        return 0
    return n%10 + temp(n//10)
def temp(n):
    return dsum(n)
num=int(input("enter a 4 digit number:"))
print("sum of digit:", dsum(num))

def A(n):
    if n<=0:
        return
    print("teja",n)
    B(n-1)
def B(n):
    if n<=0:
        return 
    print("pallagani",n)
    A(n-1)
num=int(input("enter a number:"))
A(num)
