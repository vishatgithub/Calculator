class Calculator:
    def add(self,a,b):
        ans = a + b
        print("add =",ans)
    def sub(self,a,b):
        ans = a-b
        print("sub =",ans)
    def mul(self,a,b):
        ans = a*b
        print("mul =",ans)
    def div(self,a,b):
        ans = a/b
        print("div = ",ans)

class AdvanceCalculator (Calculator):
    def sqr(self,n):
        print("sqr = ", n*n)

    def cube(self,n):
        print("cube = ", n*n*n)
        
ac = AdvanceCalculator()
ac.sqr(5)
ac.cube(5)
ac.add(10,20)
ac.sub(10,5)

#laptop-->p
dell,lenovo,
