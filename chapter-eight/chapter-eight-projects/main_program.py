from module import repeat_name as rp

name = input("Give me your first name:\n")
last_name = input("Give me your last name:\n")
full_name = rp(name, last_name)

print(f"Hello {full_name}")
