num=int(input("Enter a number"))
fact=1
if num<0:
  print("negative number")
elif num==0:
  print("the factorial of given number 0")
else:
  for i in range (1,num+1):
      fact=fact*i
      print(fact)