def my_func(*args):  
    for arg in args:  
        print (arg) 
    
my_func('Hello', 'darkness', 'my', 'old', 'friend') 

def new_func(arg1, *args):  
    print("Arg 1: ",arg1)
    for arg in args:  
        print (arg) 

new_func('Hello', 'darkness', 'my', 'old', 'friend') 