cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capicity = cars_driven * space_in_a_car
average_passengers_in_a_car = passengers / cars_driven


print("There are", cars,"cars avalible.")
print("There are only", drivers,"drivers avalible.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can tronsport", carpool_capicity,"people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_in_a_car,"in each car.")