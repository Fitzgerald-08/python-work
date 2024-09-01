guest_list = ["Akira Toriyama", "Eiichiro Oda", "Tite Kubo"]

print(f"{guest_list[1]} won´t come to the dinner\n")

guest_list[1] = "Masashi Kishimoto"

guest_list.insert(0, "One")
guest_list.insert(2, "Yukinobu Tatsu")
guest_list.append("Masami Kurumada")


# This is a very important singularity about the pop() method, so pay close attention to it

first_out = guest_list.pop(0)
second_out = guest_list.pop(0)
third_out = guest_list.pop(1)
fourth_out = guest_list.pop(1)

print(f"Sorry {first_out}, but now you can't come to the dinner")
print(f"Sorry {second_out}, but now you can't come to the dinner")
print(f"Sorry {third_out}, but now you can't come to the dinner")
print(f"Sorry {fourth_out}, but now you can't come to the dinner\n")

print(f"Hey {guest_list[0]}, you are still invited to the party")
print(f"Hey {guest_list[1]}, you are still invited to the party")

del guest_list[0]
del guest_list[0]

print(guest_list)
