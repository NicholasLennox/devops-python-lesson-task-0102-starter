def validate_non_negative(value): 
    if value < 0: 
       raise ValueError("Value cannot be negative") 
 
    return True 
 
def validate_percentage(value):
    if(value < 0 or value > 100):
        raise ValueError("Please enter a number between 0-100")
    
    return True