def validate_non_negative(value): 
   if value < 0: 
       raise ValueError("Value cannot be negative") 
 
   return True 
