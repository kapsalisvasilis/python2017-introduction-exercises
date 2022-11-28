def is_palindrome(x):
    x=list(x)
    if len(x)==0 or len(x)==1:
        return True
        
    
    if x[0]==x[-1]:
        del x[0]
        del x[-1]
        return is_palindrome(x)
    else:
        return False
    
a=input('ad:')
print(is_palindrome(a))
        
        
        
