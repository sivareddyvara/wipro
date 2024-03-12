class Siva:
    def outer(self,f1):
        def inner(self,a,b):
            try:
              result=f1(a,b)
              return result
            except ZeroDivisionError:
              print('Division by zero accured')
              return None
        return inner

    def f1(self,a,b):
        return a/b
s=Siva()
a=s.f1(a,b)
print(a)
      
      
      
  
      
      
