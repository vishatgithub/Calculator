'''
def add(a,b):
    ans=a+b
    return ans
fn=int(input("Enter first num"))
sn=int(input("Enter second num"))
print( add(fn,sn) )

def sub(a,b):
    ans=a-b
    return ans
fn=int(input("Enter first num"))
sn=int(input("Enter second num"))
print( sub(fn,sn) )

def mul(a,b):
    ans=a*b
    return ans
fn=int(input("Enter first num"))
sn=int(input("Enter second nuum"))
print( mul(fn,sn) )

def div(a,b):
    ans=a/b
    return ans
fn=int(input("Enter first num"))
sn=int(input("Enter second num"))
print( div(fn,sn) )


#square root
def square(s):
    ans=s*s
    return ans
s=int(input("Enter value:"))
print(square(s))


#cube
def cube(c):
    ans=c*c*c
    return ans
c=int(input("Enter value"))
print(cube(c))
'''

#avg of 2 sem
def marks(sem1,sem2):
    ans=(sem1+sem2)/2
    return ans

sem1=float(input("Enter marks"))
sem2=float(input("Enter marks"))
print(marks(sem1,sem2))
