def febonacci_recursion(n):
    if(n<=1):
        return n
    else:
        return(febonacci_recursion(n-1) + febonacci_recursion(n-2))

f=int(input("Enter a number: "))
for i in range(f):
    print(febonacci_recursion(i),end=" ")
              
