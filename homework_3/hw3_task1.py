def func_divide(arg1, arg2):
    try: return round((arg1/arg2), 4)
    except Exception as err:
        return err


arg1 = float(input('input the value of dividend: '))
arg2 = float(input('input the value of divider: '))
print(func_divide(arg1, arg2))