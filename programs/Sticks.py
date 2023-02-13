from random import randint

MNswitch = False


def player_turn(sticks: int):
    print(f'\n there are {sticks} sticks reamining')
    remove = 0
    while (remove > 3 or remove < 1):
        remove = int(input('how many would you like to remove? [1, 2, 3]): '))
    return remove


def ai_turn(sticks: int):
    ai_choice = randint(1, 3)
    return ai_choice


def hard_ai_turn(sticks: int, player_choice: int):
    global MNswitch
    # No extensive calculation need be made here, the player has already lost
    if MNswitch == True:
        return ((-player_choice) % 3) + 1

    magic_number = (sticks - 1) % 4  # Inverse of 4(n+1) is (n-1)/4.
                                     # If remainder is 0, num of sticks is 4n+1.
    if magic_number == 0:  # we're already at 4n+1
        return ai_turn(sticks)
    else:
        MNswitch = True
        return magic_number


def main():
    numsticks = 0
    while (numsticks < 10):
        numsticks = int(input("Choose a number of sticks to start with (atleast 10): "))

    difficulty = 0
    while difficulty != 1 and difficulty != 2:
        difficulty = int(input("\nSelect an ai difficulty: 1(easy) or 2(hard): "))

    turn = randint(0, 1)
    player_enum = {0: "AI Player", 1: "Human Player"}
    player_choice = 0
    while (numsticks > 0):
        if turn == 1:
            player_choice = player_turn(numsticks)
            numsticks -= player_choice
        else:
            ai_choice = 0
            if difficulty == 1:
                ai_choice = ai_turn(numsticks)
            else:
                ai_choice = hard_ai_turn(numsticks, player_choice)
            numsticks -= ai_choice
            print(f'\nthe ai removes {ai_choice} sticks from the pile')

        if numsticks <= 0:
            print(f'\nThe {player_enum[turn]} has draw the last stick.')
            print(f'The {player_enum[turn]} loses!')
        turn = ((turn + 1) % 2)


if __name__ == "__main__":
    main()
