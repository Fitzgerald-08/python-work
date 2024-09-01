cubes = []
for value in range(1, 11):
    cube_value = value ** 3
    cubes.append(cube_value)

print(cubes)

# In the following lines of code I will be doing the exact same thing as in the code above, but here, I will be using
# the so-called 'list comprehension'

snd_cubes = [snd_value ** 3 for snd_value in range(1, 11)]
print(snd_cubes)
