

def ret(first, second, *rest):
    return first, second, rest

#print(ret('hello', 'man', 'two', 'four', 'five'))

a,b, c = ret('hello', 'man', 'two', 'four', 'five')
print(a)
print(c)