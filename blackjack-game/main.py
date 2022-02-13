import random
from Art import logo
from turtle import clear



# 2 create a deal_card() function that uses a list below to return a random card.
def deal_card():
    """returns a random cards in the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """calculate the sum of cards in the list of cards and return the total"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

        return sum(cards)

# def compare(user_score, computer_score):
#     if user_score > 21 and computer_score > 21:
#         return "You went over, You lose 😭"
#     elif computer_score == 0:
#         return "Opponent has blackjack, You lose 😭 "
#     elif user_score == 0:
#         return "You win with Blackjack!🤑 "
#     elif user_score > 21:
#         return "You went over, You lose 😭."
#     elif computer_score > 21:
#         return "opponent went over, You win🤑."
#     elif computer_score == user_score:
#         return "Draw😶"
#     else:
#         return "You lose 😭. "

# return user and computer card
# def play_game():
print(logo)
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    print(user_cards.append(deal_card()))
    print(computer_cards.append(deal_card()))


#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(user_cards)
#
#         print(f"Your card: {user_cards}, current score: {user_score}")
#         print(f"computer's first card: {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             '''Ask the user if they want to draw another card'''
#             draw_card = input("Want to gt another card? Type 'y' or 'n': ")
#             if draw_card == 'y':
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#         while computer_score != 0 and computer_score < 17:
#             computer_cards.append(deal_card())
#             computer_score = computer_score(computer_cards)
#
#         print(f"  Your final hand: {user_cards}, final score: {user_score}.")
#         print(f"  Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
#         print(compare(user_score, computer_score))
#
#
# while input("Want to play Blackjack Game? Type 'y' or 'n': ") == 'y':
#     clear()
#     play_game()


