def summ(numbers, S):
    for i in numbers:
        S=S+float(i)
    return (S)


S=0
while(True):
    numbers=list(input('enter numbers through the space(enter q to exit): ').split(' '))
    if(numbers[-1] == 'q'):
        break
    else:
        S = summ(numbers, S)
        print(f'Summ : {S}')
print(f'Summ : {summ(numbers[0:-1:1],S)}')