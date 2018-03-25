### configuration ###
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
### end of configuration ###

# definition of the restaurant class 
class Restaurant(Base):
		# defining table name
	__tablename__ = 'restaurant'
		# defining primary key
	id = Column(Integer, primary_key=True)
		# defining name field
	name = Column(String(250), nullable=False)
# definition of the menuitem class
class MenuItem(Base):
		# defining table name
	__tablename__ = 'menu_item'
		# defining name field
	name = Column(String(80), nullable=False)
		# defining primary key
	id = Column(Integer, primary_key=True)
		# defining description field
	description = Column(String(250))
		# defining price field
	price = Column(String(8))
	# defining course field
	course = Column(String(250))
	# defining resraurant id as a foreign key
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
		# making a relationship between  Restaurant and MenuItem tables
		# using the foreign key restaurant_id
	restaurant = relationship(Restaurant)
# definition of the Employee class
class Employee(Base):
		# define table name
	__tablename__ = 'employee'
		# defining primary key
	id = Column(Integer, primary_key=True)
		# defining name field
	name = Column(String(250), nullable=False)
	# definition of the Address class
class Address(Base):
		# define Address name
	__tablename__ = 'address'
		# defining primary key
	id = Column(Integer, primary_key=True)
		# defining street field
	street = Column(String(80), nullable=False)
		# defining zip field
	zip = Column(String(5), nullable=False)
		# defining employee id as a foreign key
	employee_id = Column(Integer, ForeignKey('employee.id'))
		# making a relationship between  Employee and Address tables
		# using the foreign key employee_id
	employee = relationship(Employee)

### goes at the end of the file ###
	# create database file restaurantmenu.db
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
