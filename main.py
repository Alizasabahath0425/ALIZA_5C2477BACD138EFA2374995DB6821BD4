#implement a program to find  a recurrsive factorial number
# recursive factorial function
def factorial(n):
    if n==0:
      return 1
      
    else:
      return n*factorial(n-1)
      
# Driver code
n=int(input("Enter a number:"))
            
print("factorial of",n,"is",factorial(n))


            


