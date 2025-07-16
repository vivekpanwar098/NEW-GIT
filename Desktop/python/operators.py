#find a the sum of 3 digit number entered by the user
number=int(input('Enter a 3 digit number = '))

a=number%10
number=number//10

b=number%10
number=number//10

c=number%10
number=number//10
print(a+b+c)