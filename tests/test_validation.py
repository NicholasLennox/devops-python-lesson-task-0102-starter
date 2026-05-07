import pytest 
from validation import validate_non_negative 
 
def test_validate_non_negative_accepts_positive_numbers(): 
   result = validate_non_negative(10) 
 
   assert result is True 
 
def test_validate_non_negative_rejects_negative_numbers(): 
   with pytest.raises(ValueError): 
       validate_non_negative(-5)    


