"""
In Python, if you separate multiple values with commas and don't explicitly put them inside 
a container like a list or tuple, Python will automatically create a tuple.
"""
def add(a,b):
    return a+5,b+5
result=add(3,2)
print(result)