from sys import argv

script, user_name = argv, argv
prompt = 'Enter here:'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
live = input(prompt)

print("What kin do computer do you have?")
computer = input(prompt)

print(f"""
Alright, you said {likes} about liking me. 
You live in {live}. Not sure where that is.
And you have a {computer} computer. Nice.
""")