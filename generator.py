def fibonacci(max_value):
    a,b=0,1
    while a<max_value:
        yield a
        a,b=b,a+b
        
for number in fibonacci(1000):
    print(number)
    
####### example 2 ###################

g=(i for i in range(5))
print(type(g))