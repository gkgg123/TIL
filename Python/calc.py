def my_sum(a,b):
    return a+b
def my_minus(a,b):
    return a-b

def my_multiple(a,b):
    return a*b

def my_divide(a,b):
    try:
        num1=a/b
        return num1
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'