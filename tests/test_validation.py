import pytest 
from validation import validate_non_negative, validate_percentage 
 
def test_validate_non_negative_accepts_positive_numbers(): 
   result = validate_non_negative(10) 
 
   assert result is True 
 
def test_validate_non_negative_rejects_negative_numbers(): 
   with pytest.raises(ValueError): 
       validate_non_negative(-5)    

def test_validate_percentage_valid_number():
   # Arrange
   value = 50

   # Act
   result = validate_percentage(value)

   # Assert
   assert result is True

def test_validate_percentage_lower_bound():
   # Arrange
   value = 0

   # Act
   result = validate_percentage(value)

   # Assert
   assert result is True

def test_validate_percentage_upper_bound():
   # Arrange
   value = 100

   # Act
   result = validate_percentage(value)

   # Assert
   assert result is True

def test_validate_percentage_below_valid_should_throw():
   # Arrange
   value = -1
   error_text = "Please enter a number between 0-100"

   # Act + assert
   with pytest.raises(ValueError) as error:
      validate_percentage(value)

   # Assert
   assert str(error.value) == error_text

def test_validate_percentage_above_valid_should_throw():
   # Arrange
   value = 101
   error_text = "Please enter a number between 0-100"

   # Act + assert
   with pytest.raises(ValueError) as error:
      validate_percentage(value)

   # Assert
   assert str(error.value) == error_text
