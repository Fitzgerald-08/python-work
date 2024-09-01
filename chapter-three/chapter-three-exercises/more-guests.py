guest_list = ["Akira Toriyama", "Eiichiro Oda", "Tite Kubo"]

print(f"{guest_list[1]} won´t come to the dinner\n")

guest_list[1] = "Masashi Kishimoto"

print("Hey, guess what? I just found a bigger table, so i'll invite more people to the dinner")

guest_list.insert(0, "One")
guest_list.insert(2, "Yukinobu Tatsu")
guest_list.append("Masami Kurumada")

print(f"Invitation for {guest_list[0]}")
print(f"Invitation for {guest_list[1]}")
print(f"Invitation for {guest_list[2]}")
print(f"Invitation for {guest_list[3]}")
print(f"Invitation for {guest_list[4]}")
print(f"Invitation for {guest_list[5]}")
