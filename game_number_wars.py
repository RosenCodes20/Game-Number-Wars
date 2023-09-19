name_of_the_first_player = input()
name_of_the_second_player = input()
command = input()
player_one_points = 0
player_two_points = 0
difference = 0

while command != "End of game":
    card_for_first_player = int(command)
    card_for_second_player = int(input())

    difference = abs(card_for_second_player - card_for_first_player)

    if card_for_first_player > card_for_second_player:
        player_one_points += difference

    elif card_for_first_player < card_for_second_player:
        player_two_points += difference

    elif card_for_first_player == card_for_second_player:
        card_for_first_player = int(input())
        card_for_second_player = int(input())

        if card_for_first_player > card_for_second_player:
            winner = name_of_the_first_player
            winner_points = player_one_points + difference

        elif card_for_second_player > card_for_first_player:
            winner = name_of_the_second_player
            winner_points = player_two_points + difference

        print("Number wars!")
        print(f"{winner} is winner with {winner_points} points")
        break

    command = input()

else:
    print(f"{name_of_the_first_player} has {player_one_points} points")
    print(f"{name_of_the_second_player} has {player_two_points} points")
