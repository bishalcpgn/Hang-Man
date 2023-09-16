from random import choice
from os import system 
#selecting and returning actual word(lword) , returning fill with ___ to be filled by users
def select_word():
    words = "abruptly absurd abyss affix askew avenue awkward axiom azurev bagpipes bandwagon banjo bayoubeekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquicri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic"
    lword = list(choice(words.split()))
    fill = list(lword[0]+"_"*(len(lword)-1))
    return fill, lword


def start(fill, lword):
    print("\n******************************************************************************\n\n")
    print("|     |      | \\   / |   /  \   |\\   |")
    print("|_____| ____ |  \\ /  |  /    \\  | \\  |")
    print("|     |      |       |  |____|  |  \\ |")
    print("|     |      |       |  |    |  |   \\|")
    print("                                      by bishal")
    print("                                      [https://github.com/bsal1]\n")
    print("Note :")
    print("Although same wrong character is entered twice, error is counted only once.\n")
    print("")
    print("******************************************************************************")
    user_data = []#to update user inputs
    print(f'\nHint : The word has {len(lword)} letters and starts with {lword[0]}.\n')
    print(f'{"".join(fill)}\n')
    counter = 0
    while True:
        print("******************************************************************************")

        if counter != 8: #hanging man's picture will be completed in 9 wrong steps
            print(f"\nAttempt : {len(user_data)+1}")
            if len(user_data) == 20:  #max 20 attempts as all values except a-z arenot considered wrong
                print("\nToo many attempts :\n")
                break
        man(counter)
        print(f"\nYour Inputs : {user_data}")
        if counter == 8:
            print("\nYou Loss the game.")
            print(f"The word is : {''.join(lword)}")
            break
        print("\n")
        user_in = input("Enter a character : ")
        

        print("\n")
        #validating the input
        if ((len(user_in)) == 1) and (user_in.isalpha()):
            if user_in in fill or user_in in user_data :
                print("This entry already exists.")
                print(f'{"".join(fill)}\n') #converting list to string

            elif user_in in lword:
                for i in range(0, len(lword)):
                    if user_in == lword[i]:
                        fill[i] = lword[i]
                        print("Correct character !!\n")
                final = "".join(fill)
                if "_" in final: #chcecking if word is completed 
                    print(final)
                    user_data.append(user_in)
                    continue
                else:
                    print(final)
                    print("You won.")
                    break

            else:
                print(f"Wrong character !!\n ")
                counter += 1 
                print(f'{"".join(fill)}\n')

        else:
            print("Please enter characters from a-z.") #other entries except a-z are not cosidered as mistake 
            print(f'{"".join(fill)}\n') 
        user_data.append(user_in)


def man(counter):
    if counter == 0:
        print("     ______________")
        print("\t         |")
        print("\t         |")
        print("\t         |")
        print("\t         |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 1:
        print("     ______________")
        print("\t |       |")
        print("\t         |")
        print("\t         |")
        print("\t         |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 2:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t         |")
        print("\t         |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 3:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t/        |")
        print("\t         |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 4:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t/ \      |")
        print("\t         |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 5:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t/|\\      |")
        print("\t         |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 6:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t/|\\      |")
        print("\t |       |")
        print("\t         |")
        print("     ____________|__")

    elif counter == 7:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t/|\\      |")
        print("\t |       |")
        print("\t/        |")
        print("     ____________|__")

    else:
        print("     ______________")
        print("\t |       |")
        print("\t O       |")
        print("\t/|\\      |")
        print("\t |       |")
        print("\t/ \\      |")
        print("     ____________|__")


def main():
    try:
        fill, lword = select_word()
        start(fill, lword)
        while (input("\nDo you want to continue(y) ? ").lower() == "y"):
            system('clear')
            fill, lword = select_word()
            start(fill, lword)
        exit("\nThank you !!\n\n")

    except:
        exit("\nSomething wrong. Exiting !!\n\n")
if __name__ == "__main__":
    main()
