def factorial (n):
    if n==1:
        return 1
    else:
       return n*factorial(n-1)
num=float(input("enter a number:"))
print("factorial of", num,"is", factorial(num))
