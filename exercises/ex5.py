name = 'Zed A. Shaw'
age = 35
height = 74 # inches
inches_to_cm = 2.5 # bogus
height_cm = height * inches_to_cm
weight = 180 # lbs
lbs_to_kg = 0.3  # bogus
weight_kg = weight * lbs_to_kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches ({height_cm} cm) tall.")
print(f"He's {weight} pounds ({weight_kg} kg) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")
