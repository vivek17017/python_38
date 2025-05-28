"""




#Q1
def first(n):
    if n==1:
        print(2)
    else:
        first(n-1)
        print(2*n)
x=first(10)



 

#Q2
def first(n):
    if n==1:
        print(2)
    else:
        print(2*n)
        first(n-1)
x=first(10)




#Q3
def first(n):
    if n==1:
        print(1)
    else:
        first(n-1)
        print(n*n)
x=first(10)





#Q4
def first(n):
    if n==1:
        print(1)
    else:
        first(n-1)
        print(n**3)
x=first(10)

#Q5
def reverse(n):
    i,a=0,n
    while a:
        i+=1
        a=a//10

    if n<10:
        return n
    else:
        return(reverse(n//10)+(n%10)*(10**(i-1)))
    
x=reverse(34593)
print(x)


"""
#Q5
def rev(n):
    if n!=0:
        print(n%10)
        rev(n//10)
rev(123)


