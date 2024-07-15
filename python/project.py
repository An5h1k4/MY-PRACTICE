import time
import pygame
# Input name
name = input("Name your character: ")
time.sleep(1.5)
print(f"Welcome, {name}!")
time.sleep(1.5)
# Power selection
powers = ["Arsonist", "Assassin", "Knight", "Saint", "Alchemist"]
time.sleep(1.5)
print("Which power do you choose?")
for idx, power in enumerate(powers):
    print(f"{idx}: {power}")

# Power selection loop
while True:
    num = int(input("Choose the number corresponding to the desired strength: "))
    if num in range(len(powers)):
        print(f"Congratulations! You now possess the power of {powers[num]}.")
        time.sleep(1.5)
        strength = powers[num]
        break
    else:
        print("Something feels wrong... Try again.")

# Inventory function
def inventory(strength):
    weapons = []
    if strength == "Arsonist":
        weapons = ["Sword of Babalon", "Shield of Areshian Dragon"]
    elif strength == "Assassin":
        weapons = ["Cape of the Shadows", "Knife of the Wind"]
    elif strength == "Knight":
        weapons = ["Armor of Joshua", "Sword of Athena"]
    elif strength == "Saint":
        weapons = ["Blessing of God Luminas", "Staff of the Truth"]
    elif strength == "Alchemist":
        weapons = ["Potion of Life", "Book of Enchantment"]
    return weapons

# Confirmation loop
while True:
    conf = input("Continue after knowing the risks? (yes/no): ")
    if conf == "yes":
        print("\nGood... Let's see your weapons:")
        time.sleep(1.5)
        weapons = inventory(strength)
        if weapons:
            for idx, weapon in enumerate(weapons, start=1):
                print(f"{idx}. {weapon}")
                time.sleep(1.5)
        else:
            print("No weapons found for your power.")
        break
    elif conf == "no":
        print("Well, this quest is not suitable for everyone.")
        time.sleep(1.5)
        break
    else:
        print("What was that?...")

print("\nSo, you have finally taken yourself to embark on the journey.")
