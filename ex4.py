#Creates var car and sets it to int 100
cars = 100
#Creates var space in a car and sets it to float 4.0
space_in_a_car = 4
#creates var drivers and sets it to 30
drivers = 30
#Creates var passengers and sets it to 90
passengers = 90
#Creates var cars not driven and sets it equal to var cas - var drivers (above).
cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

