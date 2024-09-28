username = {
    "fitzgerald": "alex",
    "josh": "jose",

}

# In order to print only the keys in a dictionary you could either just leave it empty and print the variable assigned
# to that for loop or use the keys() method
for user_name in username.keys():
    print(f"{user_name.title()}")

# To print only the values in a dictionary, use the values() method, these way the variable in the for loop will be
# assigned only to the values of a determined dictionary
print(" ")
for real_name in username.values():
    print(f"{real_name.title()}")

# There are two ways to print the key and value of a dictionary, I can't explain how both methods work, so look at it
# until you have understood how they work
for userName, realName in username.items():
    print(f"\nName: {userName.title()}")
    print(f"Real name: {realName.title()}")

for user in username:
    print(f"\n{user.title()}: {username[user].title()}")
