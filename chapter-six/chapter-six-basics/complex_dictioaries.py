user_0 = {
    "userName": "fitzgerald",
    "realName": "alex",
    "email": "gnulinux.ftw.09@gmail.com",
    "age": 22,
    "city": "los mochis",
    "occupation": "student",

}

user_1 = {
    "userName": "josh",
    "realName": "jose",
    "email": "pizzalover.6971@gmail.com",
    "age": 20,
    "city": "oslo",
    "occupation": "student",

}

user_2 = {
    "userName": "mil3s",
    "realName": "scott",
    "email": "gallina.hen.20@gmail.com",
    "age": 28,
    "city": "copenhagen",
    "occupation": "software engineer",

}

users = [user_0, user_1, user_2]

# This is where things get fun

print(f"The following users are currently enrolled in our program: ")
for user in users:
    username = user["userName"].title()
    realname = user["realName"].title()
    email = user["email"]
    age = user["age"]
    city = user["city"].title()
    occupation = user["occupation"].title()

    print(f"\nUsername: {username}")
    print(f"Real name: {realname}")
    print(f"e-mail: {email}")
    print(f"Age: {age}")
    print(f"Location: {city}")
    print(f"Occupation: {occupation}")


