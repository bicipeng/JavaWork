'''super().__init__()
at a high level super() gives you access to methods in a superclass from the subclass that inherits from it.
super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.
'''
#example
class Rectangle():
	def __init__(self,h,w):
		self.h = h
		self.w = w

	def area(self):
		return self.h * self.w

retangle1 = Rectangle(3,4) 
print(retangle1.area()) #return 12

class Square(Rectangle): # class Square will inherit methods from superclass(Retangle)
	def __init__(self,h):
		self.h = h
		super().__init__(h,h)
	 #Here, you’ve used super() to call the __init__() of the Rectangle class,
	 # allowing you to use it in the Square class without repeating code. Square is the subclass of Rectangle
	 #The Square class inherited .area() from the Rectangle class.
	 #Because the Square and Rectangle .__init__() methods are so similar, 
	 #you can simply call the superclass’s .__init__() method (Rectangle.__init__()) from that of Square by using super().
	 # This sets the .length and .width attributes even though you just had to supply a single length parameter to the Square constructor.
	 #not passing self as param since it inherites from a superclass, not itself
class Cube(Square):
	def suface_area(self):
		output_area = super().area() * 6
		return output_area
	def volume(self):
		output_volume = super().area() * self.h
		return output_volume
'''Also notice that the Cube class definition does not have an .__init__(). 
Because Cube inherits from Square and .__init__() doesn’t really do anything differently
 for Cube than it already does for Square, you can skip defining it, and the .__init__() 
 of the superclass (Square) will be called automatically.
 Not only does this save us from having to rewrite the area calculations, 
 but it also allows us to change the internal .area() logic in a single location
 '''


	
	
cube1 = Cube(3)
print(cube1.suface_area())
print(cube1.volume())