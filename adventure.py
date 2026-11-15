print("You are standing in a central room.\n")
print("To your LEFT is a big doorway leading to a Zoo.")
print("To your RIGHT is a small doorway leading to a Garden.")

choice = input("Which direction would you like to go? (left/right): ")

if choice.lower() == "left":
    print("You have entered the Zoo. 🦁🐾🐘.\n")
    print("You see a variety of animals, including lions, tigers, and monkeys.")
    print("You can hear the sounds of the animals as you walk through the zoo.")

    print("1. Visit the animal enclosure (Play word scramble challenge)\n")
    print("2. Check the visitor center (Instant $100 lottery win!)")

    zoo_choice = input("What would you like to do? (1/2): ")

    if zoo_choice == "1":
        print("You have chosen to visit the animal enclosure. 🦁🐾")
        print("As you approach the enclosure, you see a sign with a word scramble challenge.")
        print("The scrambled word is: N O I L")
        answer = input("Unscramble the word: ")

        if answer.lower() == "lion":
            print("Correct! You have solved the word scramble challenge.\n")
            print("You receive a special animal-themed souvenir from the zoo gift shop!")
        else:
            print("Incorrect. The correct answer was 'LION'. Better luck next time!")

    elif zoo_choice == "2":
        print("You have chosen to check the visitor center. 🎟️\n")
        print("As you enter the visitor center, you see a lottery machine.")
        print("You decide to try your luck and pull the lever.")
        print("Congratulations! You have won an instant $100 lottery prize!\n 💰")
        print("You can use this money to buy souvenirs or enjoy more activities at the zoo.")

elif choice.lower() == "right":
    print("You have entered the Garden. 🌸🌿🌻")
    print("You see a beautiful garden filled with colorful flowers and lush greenery.\n")

    print("1. Relax by the fountain (Instant $100 lottery win!)")
    print("2. Walk down the flower path (Play flower word scramble)\n")

    garden_choice = input("What would you like to do? (1/2): ")

    if garden_choice == "1":
        print("You have chosen to relax by the fountain. ⛲\n")
        print("As you sit by the fountain, you feel a sense of calm and tranquility.\n")
        print("Suddenly, you notice a lottery ticket floating in the water.")
        print("You pick it up and check the numbers. Congratulations! You have won an instant $100 lottery prize! 💰\n")
        print("You can use this money to buy souvenirs or enjoy more activities in the garden.")

    elif garden_choice == "2":
        print("You have chosen to walk down the flower path. 🌺🌿🌻\n")
        print("As you stroll along the path, you see a sign with a flower word scramble challenge.")
        print("The scrambled word is: S E R O\n")
        answer = input("Unscramble the word: ")

        if answer.lower() == "rose":
            print("Correct! You have solved the flower word scramble challenge.\n🌹")
            print("You receive a beautiful bouquet of roses as a reward!")
        else:
            print("Incorrect. The correct answer was 'ROSE'. Better luck next time!\n")

print("Thank you for visiting the Folktale world! We hope you enjoyed your adventure in the Zoo and Garden. 🌟\n")
print("Remember to come back and explore more magical places in the future! 🗺️✨\n")
print("Goodbye and safe travels! 🌈🚀\n")
