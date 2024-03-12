def outer(f1):
    def inner(a,b):
        try:
            result=f1(a,b)
            return result
        except ZeroDivisionError:
            print('Division by zero accured')
            return None
    return inner
@outer
def f1(a,b):
    return a/b

siva=f1(5,2)
print(siva)


def dec_outer(add):
    def inner(a,b):
        c=a *a
        d= b*b
        return add(c,d)
    return inner
@dec_outer
def add(a,b):
    return a+b

siva=add(2,3)
print(siva)

      
  
      
      
