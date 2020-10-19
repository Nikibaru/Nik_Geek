my_file = open('text_file_for_task1.txt', 'w')
#Enter the text
while (True):
    new_string = input('Enter the new string: ')
    if (new_string == ''):
        break
    else:
        my_file.write(new_string+'\n')
my_file.close()

#Delete the last empty string with '\n'
with open('text_file_for_task1.txt', 'rb+') as f:
    f.seek(0,2)
    size = f.tell()
    f.truncate(size - 1)
