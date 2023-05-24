#HANGMAN CODE PYTHON 1 FINAL PROJECT
#Zack Patterson

#RANDOM NUMBER
import random

#CORRECT WORD SELECTOR
hangman_word_list = ["Apple", "Table", "Chair", "Sun", "Moon", "Car", "Book", "Pen", "Dog", "Cat", "House", "Tree", "River", "Mountain", "Ocean", "Cloud", "Rain", "Fire", "Snow", "Phone", "Lamp", "Shirt", "Shoe", "Glass", "Key", "Clock", "Bike", "Bag", "Window", "Mirror", "Door", "Music", "Bird", "Fish", "Tablet", "Knife", "Fork", "Spoon", "Plate", "Bowl", "Cup", "Ring", "Hat", "Glove", "Socks", "Pants", "Dress", "Suit", "Tie", "Scissors", "Brush", "Paint", "Paper", "Bed", "Pillow", "Blanket", "Guitar", "Piano", "Drum", "Trumpet", "Violin", "Camera", "Movie", "Radio", "Television", "Computer", "Laptop", "Mouse", "Keyboard", "Speaker", "Headphones", "Microphone", "Game", "Ball", "Bat", "Golf", "Tennis", "Soccer", "Basketball", "Football", "Chess", "Checkers", "Snack", "Drink", "Juice", "Coffee", "Tea", "Cake", "Cookie", "Candy", "Pizza", "Burger", "Salad", "Soup", "Ice", "Rainbow", "Smile"]
random_num = random.randint(0,(len(hangman_word_list) - 1))

#DEFINGING GET WORD
def get_rand_word(words):
    return(random.choice(words))

#DEFINING MYSTERY WORD
def display_word(hangman_correct_word, guessed_letter):
    display_word = ""
    for letter in hangman_correct_word:
        if letter in guessed_letter:
            display_word += letter.upper()
        else:
                display_word += "*"
    print(display_word)
    return(display_word)

def play_hangman():
    
    #SELECTING RANDOM WORD
    hangman_correct_word = get_rand_word(hangman_word_list).upper()
    
    #USERINPUT OF WORD
    user_guess = input("\nAlright, Lets start.\nWhat is your first guess? ")
    
    #STICK FIGURE
    #note stick figure list index is 0 - 6
    stick_figure_list = ["" , "  0\n" , "  0\n  I\n" , "  0\n /I\n" , "  0\n /I\\\n" , "  0\n /I\\\n /\n" , "  0\n /I\\\n / \\\n"]
    stick_figure_strike_count = 0
    
    #GUESSED LETTERS
    guessed_letter = ""
    
    #HANGMAN GAME
    while user_guess.upper().isalpha() and len(user_guess) == 1:
        if user_guess.upper() in hangman_correct_word and user_guess.upper() not in guessed_letter:
            guessed_letter = guessed_letter + user_guess.upper()
            print(stick_figure_list[stick_figure_strike_count])
            displayed_word = display_word(hangman_correct_word, guessed_letter)
            if displayed_word == hangman_correct_word:
                print(stick_figure_list[stick_figure_strike_count])
                print("You Win!")
                break
            else:
                pass
            user_guess = input("Next Guess? ")
        elif user_guess.upper() in guessed_letter:
            print("You already guessed this Letter!")
            print(stick_figure_list[stick_figure_strike_count])
            display_word(hangman_correct_word, guessed_letter)
            user_guess = input("Next Guess? ")
        else:
            print("Nice Try, But Wrong")
            stick_figure_strike_count += 1
            print(stick_figure_list[stick_figure_strike_count])
            guessed_letter = guessed_letter + user_guess.upper()
            display_word(hangman_correct_word, guessed_letter)
            if stick_figure_strike_count == 6:
                print("You Loose!")
                print("The Correct word was" , hangman_correct_word)
                break
            else:
                pass
            user_guess = input("Next Guess? ")
            
#STICKY NOTE
#password: hangman
sticky_note = " ___________\n|           |\n| password: |\n|  hangman  |\n|___________|\n"
print(sticky_note)
#PASSWORD CODE 
def passw(passw):
    mypassw = "hangman"
    valid = False
    if password.lower() == mypassw.lower():
        valid = True
    return valid
password = input("Enter Your Password: ")
x = 0 
while x < 3:
    valid = passw(passw)
    if valid == True:
            break
    else:
        print("Invalid")
        password = input("Enter Your Password: ")
        x += 1
if valid == False:
    print("You ran out of Guesses.\nTry again later.")
    exit()

#INTRO TO GAME
name = input("\nHello User, Welcome to Hangman.\nEnter your username: ")
print("\nWelcome," , name)
user_choice = input("\nBefore we start, Would you like a reminder of the rules? [Y/N] ")
if user_choice.lower().startswith("y"):
    print("I will think of a word and the you will try to guess it by guessing letters. Each incorrect guess brings you closer to being \"hanged.\". You get 7 incorrect guesses before you get \"hanged\".\n") 
elif user_choice.lower().startswith("n"):
    print("We will pass this then")
else:
    print("That\'s not a Yes or a No, So we will continue.")

while True:
    play_hangman()
    playagain = input("\nWould you like to play play again[Y/N]: ")
    if playagain.upper() == "N":
        print("Thank You for Playing!")
        print("\n|\n \\ 0\n   M \\\n   V  |\n  / \\\n |   |\n")
        break
    else:
        continue
