#DECORATOR - search google for more

def decor(fn):
    def wrap():
        print("#$%^&*()")
        fn()
        print("#$%^&*()")
    return wrap
@decor
def echo():
    print("echo echo")
echo()
