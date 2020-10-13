# my primitive attempt to write a func for comparison, but it works fine only for positive numbers
def my_func1(arg1, arg2, arg3):
    #exception of dividing by zero
    if (arg1*arg2*arg3 == 0):
        return (arg1+arg2+arg3)
    else:
        #comparison
        if (arg1//arg3 and arg2//arg3):
            return (arg1+arg2)
        elif (arg1//arg2):
            return (arg1+arg3)
        else:
            return(arg2+arg3)

# right solution
def my_func(arg1, arg2, arg3):
    return max(arg1, arg2)+max(arg2, arg3)

#test
a, b, c = 15,0,-13
print(my_func(a,b,c))