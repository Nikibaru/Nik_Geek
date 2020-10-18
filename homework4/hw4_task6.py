from itertools import cycle, count
# part A) Where we generate integer numbers 
start_el = int(input('Enter the start number: '))
end_el = int(input('Enter the last number: '))

for el in count(start_el):
    if el > end_el:
        break
    else:
        print(el)
#Part B) Where we repeate elements from the list
l = [1,2,5,6,7,8,9]
n = int(input('enter the number of repetition: '))
p=1
for i in cycle(l):
    if p > n:
       break
    else:
        print(i)
        p+=1


