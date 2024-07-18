#def factorial(n):
    #if(n==0 or n==1):
   #     return 1
  #  else:
 #       return n * factorial(n-1)

#print(factorial(5))

def fibbonacci(f):
    if(f<=1):
        return f
    else:
          return (fibbonacci(f-1) + fibbonacci(f-2))
f = int(input("enter the value of f\n"))
for i in range(f):
    print(fibbonacci(i))



