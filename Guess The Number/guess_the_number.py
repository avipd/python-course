

amount_of_players = int(input("How many players is play ? "))
data_of_players = {}

for i in range(amount_of_players):
    counter = 0

    name_of_player = input(f"Player {i + 1} Insert your name: ")
    print("Stating game...")

    while True:
        number = int(input("Guss The Number: "))
        counter = counter + 1

        if number == 5:
            print(f"You Win With {counter} guesses")
            number_of_guesses = counter
            data_of_players[name_of_player] = number_of_guesses
            break
        else:
            print(f"Wrong")

    print(f"data_of_players = {data_of_players}")

list_from_dict = list(data_of_players.values())

min_number = list_from_dict[0]
for i in range(amount_of_players):
    if list_from_dict[i] < min_number:
        min_number = list_from_dict[i]
print(f'min_number = {min_number}')

winner = 0
for player in data_of_players.items():
    if min_number == player[1]:
        winner = player[0]
print(f'The winner is = {winner}')


# TODO: show the winner...
