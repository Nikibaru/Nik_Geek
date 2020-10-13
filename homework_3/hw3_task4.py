def power_var1(x, y):
    return round(x**y , 8)

def power_var2(x, y):
    if(x != 0):
        y=y+1
        if (abs(y)==0):
            return (1/x)
        else:
            x = power_var2(x, y)/x
        return round(x, 8)
    else:
        return(0)

#test
print(power_var1(3.45, -6) , power_var2(3.45, -6))