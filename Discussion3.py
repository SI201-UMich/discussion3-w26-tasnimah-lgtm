import math

class Rectangle():
    # Create the constructor "__init__" method
          
    # YOUR CODE HERE
   def __init__(self, user_width, user_height):
        self.width = user_width
        self.height = self_height
        
    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}" 

    # Create the "area_calculator" method
  

    # YOUR CODE HERE
def area_caculator(self):
        return float(self.length * self.width)
    
  # Create the "__eq__" method
    #
    # Returns a boolean value

    # YOUR CODE HERE
    def __eq__(self,other):
     if isinstance(other,Rectangle):
          return self.length == other.length and self.width == other.width
     return False





