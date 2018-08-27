#excercise 1 : whats the output?

def exlist2(val, chuck=[]):
    chuck.append(val)
    return chuck
list1=exlist2(10)
list2 = list(exlist2(10)) # this gives output of [10]
list3=exlist2('a')
list4=exlist2(100,[])
print(list1,list2,list3,list4)

# You’d expect the output to be something like this:
# ([10],[10],[123],[‘a’])
# Well, this is because the list argument does not initialize to its default
#  value ([]) every time we make a call to the function. Once we define the
#  function, it creates a new list. Then, whenever we call it again without a
#  list argument, it uses the same list. This is because it calculates the
#  expressions in the default arguments when we define the function,
#  not when we call it.
