def my_sqrt(x):
    num1=1
    num2=x
    while True:
        mid=(num1+num2)/2
        if round(mid**2,3)==x:
            return mid
        elif mid**2<x<num2**2:
            num1=mid
        elif num1**2<x<mid**2:
            num2=mid
print(my_sqrt(2))