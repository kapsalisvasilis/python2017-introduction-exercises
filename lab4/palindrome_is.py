def is_palindrome(x):
    z=list(x)
    y=list(reversed(x))
    if z==y:
        return True
    else:
        return False
a=input('enter word:')
print(is_palindrome(a))
