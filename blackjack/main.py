import random
import time

main_deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def draw_card(deck):
	deck.append(random.choice(main_deck))


def find_total(deck):
	total = 0
	ace_counter = 0
	for card in deck:
		if card == "A":
			total += 11
			ace_counter += 1
		elif card == "J" or card == "Q" or card == "K":
			total += 10
		else:
			total += card
		if total > 21 and ace_counter > 0:
			total -= 10
			ace_counter -= 1
	return total


def print_hands():
	print("-------------------------")
	print(f"Your hand and its total:")
	print(f"{player_hand} = {find_total(player_hand)}")
	print(f"Dealers hand and its total:")
	print(f"{dealer_hand} = {find_total(dealer_hand)}")
	print("-------------------------")


def game():
	player_total = find_total(player_hand)
	dealer_total = find_total(dealer_hand)
	while player_total <= 21 and input("Stand or Draw?\n") == "d":
		draw_card(player_hand)
		player_total = find_total(player_hand)
		print_hands()

	if player_total > 21:
		print(f"Busted. You lost.")
		return

	while dealer_total < 17:
		print("Dealer will draw.")
		time.sleep(2)
		draw_card(dealer_hand)
		dealer_total = find_total(dealer_hand)
		print_hands()

	if dealer_total > 21:
		print("Dealer busted. You win.")
	elif dealer_total == player_total:
		print("It is a draw.")
	elif dealer_total > player_total:
		print(f"Dealer is closer to 21. You lost.")
	else:
		print("You are closer to 21. You win.")


reset_game = True
while reset_game:
	player_hand = [random.choice(main_deck), random.choice(main_deck)]
	dealer_hand = [random.choice(main_deck)]
	print_hands()
	game()
	reset_game = True if input("A to Play Again: ").lower() == "a" else False
