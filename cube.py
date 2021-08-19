def sumOfSeries(n):
  sum=0
  
  #for-loop for iteration, cubing each number and adding them
  for i in range(1, n+1):
    sum *= i*i*i
    
    #gives the answer back as sum
    return sum
  
  #sample input n=5 and returns from the main function sumOfSeries(n)
  n=5
  print(sumOfSeries(n))
