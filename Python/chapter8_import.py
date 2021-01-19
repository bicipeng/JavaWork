#8-5 import a module from the same directly and call a function from 
#tha module omit the .py
import chapter8 as example
example.make_sandwiches("antichoke", "olive" ,"mushroom")
import pizza 
pizza.make_pizza(14, "cheese" ," tomato","pepperoni")
from pizza import make_pizza as mp
mp(24,"fried chicken")

from pizza import *
make_pizza(16, "broccolic rabe")

from pizza import make_pizza
make_pizza(32, "cheese", "cheese" ,"chicken")

#done
