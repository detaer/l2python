name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue' # color noob
teeth = 'White'
hair = 'Brown'

pound_to_kilo = 0.453592
inch_to_cm = 2.54

weight_in_kilo = weight * pound_to_kilo
height_in_cm = inch_to_cm  * height

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually That's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(f"If you use space points he is {height_in_cm} cm tall and {weight_in_kilo} kilos fat.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")
rounded_weight_in_kilo = round(weight_in_kilo)
rounded_height_in_cm = round(height_in_cm)
print(f"This looks nicer {rounded_weight_in_kilo}")
print(f"This looks nicer {rounded_height_in_cm}")
