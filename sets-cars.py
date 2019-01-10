# 1. Create an empty set named showroom.
showroom = set()
# 2. Add four of your favorite car model names to the set.
showroom.add("PT Crusier")
showroom.add("Scion xB")
showroom.add("Mazda 3")
showroom.add("VW Bus")
# 3. Print the length of your set.
print(len(showroom))
# 4.Pick one of the items in your show room and add it to the set again.
showroom.add("Scion xB")
# 5. Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)
# 6. Using update(), add two more car models to your showroom with another set.
# this is how lesley did it
new_cars = set({"Kia Rio", "Fiat 500"})
showroom.update({"Kia Rio", "Fiat 500"})
print(showroom)
# how andy did it
showroom.update({"Kia Rio", "Fiat 500"})
# 7. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Kia Rio")
print(showroom)

# ***************************
# One is a print and the second group of code is running it through a function
# ***************************
# print(showroom)
# print(f"Our showroom contains {showroom} and I have {len(showroom)} cars in it")

# def say_showroom():
#   print(f"Our showroom contains {showroom} and I have {len(showroom)} cars in it")
#   return

# say_showroom()
# ***************************
# This will loop over our showroom and show each individual car in our showroom
# ***************************
# my_showroom = []
# for taco in showroom:
#   print(f"Our showroom contains {taco} and I have {len(showroom)} cars in it")
# ****************************


# *********************************************************************************
# * Acquiring more cars
# *********************************************************************************
# 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Plymouth Voyager", "Chrysler Lebaron", "Scion xB", "Fiat 500"}
# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
crossover_results = showroom.intersection(junkyard)
print(crossover_results)
# 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
union_results = showroom.union(junkyard)
print(union_results)
# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
junkyard.discard("Plymouth Voyager")
print(junkyard)
