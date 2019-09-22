def escolher_subst_enc(c):
    if c == 'x':
        return 'a'
    
    elif c == 'y':
        return 'b'
    
    elif c == 'z':
        return 'c'
    
    elif c == 'X':
        return 'A'
    
    elif c == 'Y':
        return 'B'
    
    elif c == 'Z':
        return 'C'
    
    else:
        return c
    
def escolher_subst_dec(c):
    if c == 'a':
        return 'x'
    
    elif c == 'b':
        return 'y'
    
    elif c == 'c':
        return 'z'
    
    elif c == 'A':
        return 'X'
    
    elif c == 'B':
        return 'Y'
    
    elif c == 'C':
        return 'Z'
    
    else:
        return c