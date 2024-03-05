x = input('please enter something: ')
if x.isdigit():
    print('x is number')
elif ',' in x :
    print('x is list')
else :
    print('x is string')