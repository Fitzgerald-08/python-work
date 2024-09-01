my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

my_foods.append("cannoli")
friends_foods.append("ice cream")

print("My favorite foods are:")
for myFoods in my_foods:
    print(myFoods.title())

print("\nMy friend's favorite foods are:")
for friendsFoods in friends_foods:
    print(friendsFoods)