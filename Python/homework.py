# def my_sqrt(x):
#     num1=0
#     num2=x
#     while True:
#         mid=(num1+num2)/2
#         if round(mid**2,12)==x:
#             return mid
#         elif mid**2<x<num2**2:
#             num1=mid
#         elif num1**2<x<mid**2:
#             num2=mid
# print(my_sqrt(2))

def sqrt(n):
    left,right=1,n
    result=1
    while abs((result**2)-n)>0.0001:
        result=(left+right)/2
        if result**2<n:
            left =result
        elif result**2>n:
            right=result
    return result

print(sqrt(2))