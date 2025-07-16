# agr koi password bhul jaye to fir se dal ne k liye code
Email=input('Enter your email id = ')
password=input('Enter your password')
if Email=='vivekpanwar@gmail.com' and password == '1234':
    print('wlcome')
elif Email=='vivekpanwar@gmail.com' and password != '1234':
    print('incorrect password')
    password = input('Enter password again = ')
    if password == '1234' :
        print('welcome finally!')
    else:
        print('beta tum se na ho paye ga')
    
else:
    print('fir se dal bhai')