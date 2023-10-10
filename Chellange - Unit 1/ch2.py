def funct(n):
    s=1
    i=1
    for i in range(n):
        s=s*(i+1)
    return s
n=int(input("Enter the number :"))
print("Factorial {} is the value of {}".format(n,funct(n)))
