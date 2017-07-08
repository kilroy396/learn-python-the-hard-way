# the en' '. tells print to not end the line with a newline character
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy")
