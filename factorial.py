#main function for factorial
def factorial(n):

#return 1 or give the factorial of a number in input as a result in if-else condition
  if(n==0 || n==1)
       return 1
  else
      n * factorial(n-1)
      
 #returns the result of the factorial of num n
 num = 5
 printf("Factorial of a number is:", factorial(n))
