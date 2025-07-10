# Format Strings!!!
b = 'Ronaldo'
c = '40'
print(f'His name is {b}. He is {c} years old.')
print('His name is {}. He is {} years old.'.format(b,c))

s = "pyPYeijfsf"
print('py' in s)
print('PY' in s)
print('pY' in s)
print('Ye' in s)

email = input("enter: ")
if '@' in email and email.endswith('.com'):
    print("valid")
else:
    print("invalid")
