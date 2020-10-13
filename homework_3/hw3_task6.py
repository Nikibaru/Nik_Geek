def int_func(word):
    return word.capitalize()

test_string = 'it is the test string for int_func'

s=''
for i in test_string.split(' '):
    s = f'{s} {int_func(i)}'
print(s[1::])