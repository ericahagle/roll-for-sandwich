# Import the random library for dice rolls
import random
# Import data.py to utilize data sets
import data


# Setup the game:
"""Setup all the functions we need to run the game: die_roll, roll_for_bread, roll_for_main, roll_for_cheese, roll_for_roughage, roll_for_wild_magic, roll_for_sauce, sandwich_rating, sandwich_name, roll_for_sandwich, do_it_again"""

# Function for rolling dice
def die_roll(int1, int2):
	"""Rolls a die (number of sides determined by each sandwich element's function) and returns the result"""

	print("🎲 Type 'roll' or 'r' to roll the die.")

	while True:

		roll = input("> ")
		roll = roll.lower()

		if roll == "roll" or roll == "r":
			rolled = random.randint(int1, int2)
			print()
			print(f"You rolled: {rolled}.")
			return rolled
		else:
			print()
			print("Sorry, that's not an option. Please type 'roll' or 'r' to roll the die.")


# Function to roll for bread
def roll_for_bread():
	"""Rolls a d6 and returns the result for bread"""

	print("🍞 Alright, let's roll a d6 for bread!")
	print()
	for bread in data.bread_list:
		print(bread)
	print()
	bread_roll = die_roll(1, 6)
	bread_roll = data.bread_list[bread_roll - 1][1]
	return bread_roll


# Function to roll for main
def roll_for_main():
	"""Rolls a d10 and returns the result for main"""

	print("🍖 Ok, let's roll a d10 for our main!")
	print()
	for main in data.main_list:
		print(main)
	print()
	main_roll = die_roll(1, 10)
	main_roll = data.main_list[main_roll - 1][1]
	return main_roll


# Function to roll for cheese
def roll_for_cheese():
	"""Rolls a d8 and returns the result for cheese"""

	print("🧀 Next up, let's roll a d8 for cheese!")
	print()
	for cheese in data.cheese_list:
		print(cheese)
	print()
	cheese_roll = die_roll(1, 8)
	cheese_roll = data.cheese_list[cheese_roll - 1][1]
	return cheese_roll


# Function to roll for roughage
def roll_for_roughage():
	"""Roll a d12 and returns the result for roughage"""

	print("🥬 Next up, let's roll a d12 for roughage!")
	print()
	for roughage in data.roughage_list:
		print(roughage)
	print()
	roughage_roll = die_roll(1, 12)
	roughage_roll = data.roughage_list[roughage_roll - 1][1]
	return roughage_roll


# Function to roll for wild magic
def roll_for_wild_magic():
	"""Rolls a d20 and returns the result for wild magic"""

	print("✨ Alright, time to bring the chaos... let's roll our d20 to hit it with some wild magic!")
	print()
	for wild_magic in data.wild_magic_list:
		print(wild_magic)
	print()
	wild_magic_roll = die_roll(1, 20)
	wild_magic_roll = data.wild_magic_list[wild_magic_roll - 1][1]
	return wild_magic_roll


# Function to roll for sauce
def roll_for_sauce():
	"""Rolls a d20 and returns the result for sauce"""

	print("🥫 Aaaaaand last but not least, let's roll a d20 for sauce!")
	print()
	for sauce in data.sauce_list:
		print(sauce)
	print()
	sauce_roll = die_roll(1, 20)
	sauce_roll = data.sauce_list[sauce_roll - 1][1]
	return sauce_roll


# Function to rate the sandwich
def sandwich_rating():
	"""Returns the rating of the sandwich, as a float, given by the user"""

	print("Let's give this sandwich a rating. You can give it anything from 0 to 10, including decimals.")

	while True:

		rate = float(input("> "))

		if rate > 0 and rate < 10:
			print()
			print(f"Yep, {rate} seems fair.")
			print()
			return rate

		else:
			print()
			print("Sorry, that's out of our range. Please pick something between 0 and 10.")


# Function to name the sandwich
def sandwich_name():
	"""Returns the name of the sandwich, in title case, given by the user"""

	print("And let's give it a name, too.")
	name = input("> ")
	name = name.title()
	print()
	print(f"'{name}' sounds about right.")
	print()
	return name


# Function to play again
def do_it_again():
	"""Handles if the user wants to play again, or end the program using a while loop"""

	print("Type 'yes' or 'y' to build another sandwich, or type 'no' or 'n' to exit the program.")

	while True:

		answer = input("> ")
		answer = answer.lower()

		if answer == "yes" or answer == "y":
			print()
			return True

		elif answer == "no" or answer == "n":
			print()
			return False

		else:
			print()
			print("Sorry, I didn't get that. This is a '[y]es' or '[n]o' question, friend! Try again?")


# Main function to play the game
def roll_for_sandwich():
	"""Calls all appropriate functions to play the game and ask if the user would like to play again using a while loop"""

	while True:

		bread = roll_for_bread()
		print(f"🍞 That's {bread} 🍞.")
		print()

		main = roll_for_main()
		print(f"🍖 That's {main} 🍖.")
		print()

		cheese = roll_for_cheese()
		print(f"🧀 That's {cheese} 🧀.")
		print()

		roughage = roll_for_roughage()
		print(f"🥬 That's {roughage} 🥬.")
		print()

		wild_magic = roll_for_wild_magic()
		print(f"✨ That's {wild_magic} ✨.")
		print()

		sauce = roll_for_sauce()
		print(f"🥫 That's {sauce} 🥫.")
		print()

		# Bringing it all together
		print(f"Welp. There we have it folks... {main} 🍖, {cheese} 🧀, and {roughage} 🥬 with {wild_magic} ✨  and {sauce} 🥫 on {bread} 🍞.")
		print()

		rating = sandwich_rating()
		named = sandwich_name()

		print(f"Alrighty, you gave that sandwich a {rating} and called it '{named}'.")
		print()

		print("🎲 🥪 Would you like to build another sandwich? 🥪 🎲")
		if not do_it_again():
			print("🎲 🥪 Thanks for playing! Let's do lunch again soon! 🥪 🎲")
			break
