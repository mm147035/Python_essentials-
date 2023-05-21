import random


def draw_card():
    """Return a random card value between 1 and 10."""
    return random.randint(1, 10)


def play_game():
    """Play a game of 21."""
    player_score = 0
    dealer_score = 0

    # Draw two cards for the player and one for the dealer
    player_score += draw_card()
    player_score += draw_card()
    dealer_score += draw_card()

    print(f"Your score is {player_score}")

    # Ask the player if they want to draw another card
    while True:
        draw_another = input("Do you want to draw another card? (y/n) ")
        if draw_another == 'y':
            player_score += draw_card()
            print(f"Your score is {player_score}")
            if player_score > 21:
                print("You bust! Dealer wins.")
                return
        else:
            break

    # Dealer draws until their score is at least 17
    while dealer_score < 17:
        dealer_score += draw_card()

    print(f"Dealer's score is {dealer_score}")

    # Determine the winner
    if dealer_score > 21:
        print("Dealer busts! You win.")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie.")


play_game()
