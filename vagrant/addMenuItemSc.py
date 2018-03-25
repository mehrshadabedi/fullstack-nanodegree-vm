# This is a script to manipulate the Restaurant database
# This script is also used to add new employee
	###Configurations for database###
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
	# import from the dabase_setup file created by Mehrshad
from database_setup import Base, Restaurant, MenuItem, Employee, Address
	# The name of the database file is specified in the
	# database_setup file
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
	###End of Configurations###

	# create Pizza Palace Table Restaurant
myFirstRestaurant = Restaurant(name = "Pizza Palace")
	# add restaurant to session
session.add(myFirstRestaurant)
# commit restaurant to session
session.commit()
# quesry retaurant table
session.query(Restaurant).all()
	# Create Menu Item Cheese Pizza
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mazaralla", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
	# add menu item
session.add(cheesepizza)
	# commit menu item
session.commit()
	# querry all menu items
session.query(MenuItem).all()

### Adding new employee ###

newEmployee = Employee(name = "Rebecca Allen")
session.add(newEmployee)
session.commit()
session.query(Employee).all()
rebeccaAddress = Address(street = "512 Sycamore Road",zip = "02001", employee = newEmployee)
session.add(rebeccaAddress)
session.commit()
session.query(Address).all()	
session.query(Restaurant).all()
items = session.query(MenuItems).all()
for item in items
	print item.name
