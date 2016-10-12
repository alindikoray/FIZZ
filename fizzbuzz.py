def fizz_buzz(x):
  """ The funtion returns 'Fizz' if the number is divisible by 3,
   if divisible by 5 it returns 'buzz' and lastly 'FizzBuzz if divisible by both 3 and 5'
   """

  if x % 3 == 0 and x % 5 == 0: #if number is divisible by both 3 and 5 return 'FizzBuzz'
    return "FizzBuzz"
    
  elif x % 3 == 0: #If number is divisible by 3 return "Fizz"
    return "Fizz"
    
  elif x % 5 == 0: #if number is divisible by 5 return 'Buzz'
    return "Buzz"
    
  else:        #Else  just return the number
    return x