def Foo(v1,v2):

    if v2 < 0:
        v2 *= -1
    
    return v1 * v2

FooExp = lambda a=1, b=1, c=1: Foo(a,b) / float(c)


#-------------------------------------------------------------------#

a = [1,2,3,4,5]

a_pow2 = map(lambda x: x*x,a)

print (a_pow2)

#-------------------------------------------------------------------#

a = [1,2,3,4,-5,-3,-19,-1]

a_new = filter(lambda x: x > 0, a)
print (a)