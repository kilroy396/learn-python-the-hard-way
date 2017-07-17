from sys import argv

script, user_name, gender = argv
prompt = '-> '

if(gender == 'male'):
    salutation = "Mr"
else:
    salutation = "Mrs"

print(f"Hi {salutation} {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You like in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")