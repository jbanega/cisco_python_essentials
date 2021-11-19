# SCENARIO
# A car's fuel consumption may be expressed in many
# different ways. For example, in Europe, it is shown
# as the amount of fuel consumed per 100 kilometers.

# In the USA, it is shown as the number of miles traveled
# by a car using one gallon of fuel.

# Task: to write a pair of functions converting l/100km into mpg,
# and vice versa.
# Hints:
# 1 American mile = 1609.344 meters
# 1 American gallon = 3.785411784 liters

mile_to_meters = 1609.344
meters_to_km = 1000
gallon_to_liters = 3.785411784


def liters_100km_to_miles_gallon(liters):
    return 1 / ((liters/100) * mile_to_meters * (1/meters_to_km) * (1/gallon_to_liters))

def miles_gallon_to_liters_100km(miles):
    return 100 / (miles * (1/gallon_to_liters) * mile_to_meters * (1/meters_to_km))


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))    
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))