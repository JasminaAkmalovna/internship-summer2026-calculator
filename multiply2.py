from add2 import add 

def multiply_by_add(a, b):
    result = 0
    
    # Runing the loop 'b' times, adding 'a' to the total each time
    for _ in range(b):
        result = add(result, a)
        
    return result