import random


user_name = input("Enter your name: ")


prefixes = ["Cool", "Awesome", "Mighty", "Brave", "Quick", "Silent", "Fierce"]
suffixes = ["Warrior", "Ninja", "Samurai", "Wizard", "Knight", "Ranger", "Guardian"]


def generate_nickname(name):
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    nickname = f"{prefix}{name}{suffix}"
    return nickname


unique_nicknames = set()
for _ in range(5):  
    while True:
        nickname = generate_nickname(user_name)
        if nickname not in unique_nicknames:
            unique_nicknames.add(nickname)
            break


for nickname in unique_nicknames:
    print(nickname)
