class Rectangle:
  # Constructor to initialize width and height
  def __init__(self, width, height):
    self.height = height
    self.width = width

  # Method to set the width
  def set_width(self, width):
    self.width = width

  # Method to set the height
  def set_height(self, height):
    self.height = height

  # Method to calculate the area of the rectangle
  def get_area(self):
    return self.height * self.width

  # Method to calculate the perimeter of the rectangle
  def get_perimeter(self):
    return 2 * (self.height + self.width)

  # Method to calculate the diagonal of the rectangle
  def get_diagonal(self):
    return (self.height**2 + self.width**2)**.5

  # Method to draw the rectangle
  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      for _i in range(self.height):
        picture += '*' * self.width + '\n'
      return picture

  # Method to return the rectangle as a string
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  # Method to calculate how many times a given shape can fit inside the rectangle
  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
  # Constructor to initialize a square with a side length
  def __init__(self, side):
    # Call the constructor of the base class (Rectangle) with the side length for both width and height
    super().__init__(side, side)

  # Method to set the side length of the square
  def set_side(self, side):
    # Set both width and height to the given side length
    self.width = side
    self.height = side

  # Override the set_width method to set both width and height to the given value
  def set_width(self, width):
    self.set_side(width)

  # Override the set_height method to set both width and height to the given value
  def set_height(self, height):
    self.set_side(height)

  # Method to represent the square as a string
  def __str__(self):
    return f"Square(side={self.width})"

  # Override the get_amount_inside method to calculate how many times a given shape can fit inside the square
  def get_amount_inside(self, shape):
    # Use the side length instead of width and height in the calculation
    return (self.width // shape.width) * (self.width // shape.width)
