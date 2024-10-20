current_number = 0
while current_number < 10:  # <--- (3)
    current_number += 1
    # This block of code determines whether the number is divisible by 2, if it is, the "continue" phrase basically
    # ignores that number and returns to the beginning of the while loop (1). When "current_number" is indeed an odd
    # number, it will print it (2) and as long as "current_number" is less than 10, the code will run again until it
    # reaches the number we have set, in this case 10 (3)
    if current_number % 2 == 0:
        continue  # <--- (1)

    print(current_number)  # <--- (2)
