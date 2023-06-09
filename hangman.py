#HANGMAN CODE PYTHON 1 FINAL PROJECT
#Zack Patterson

#IMPORTING RANDOM
import random

#IMPORTING DATE
import time

#LEADERBOARD LISTS
name_list = []
time_taken = []
strike_count_list = []
category_list = []
word_list =[]

#ITEM LISTS
technology_list = ["gadget", "device", "laptop", "router", "server", "screen", "mouse", "keyboard", "camera", "drone", "sensor", "phone", "modem", "cable", "printer", "power", "drive", "sound", "radio", "cloud", "fiber", "pixel", "logic", "signal", "bytes", "memory", "coding", "python", "linux", "java", "shell", "script", "docker", "kernel", "debug", "binary", "array", "queue", "stack", "syntax", "variable", "method", "object", "class", "module", "thread", "error", "algorithm", "encryption"]
transportation_list = ["car", "train", "bike", "scooter", "plane", "truck", "bus", "taxi", "boat", "subway", "ferry", "cycle", "van", "rail", "motor", "pilot", "cargo", "wheel", "route", "tire", "speed", "drive", "road", "track", "brake", "lane", "park", "port", "fuel", "helm", "gear", "stop", "signal", "gate", "freight", "diesel", "hybrid", "traffic", "rider", "trip", "pass", "fare", "station", "bridge", "mile", "load", "route", "cargo", "destination", "commute"]
kitchen_list = ["knife", "spoon", "grater", "peeler", "plate", "glass", "bowl", "pot", "pan", "fork", "mug", "stove", "oven", "grill", "chef", "cook", "steam", "bake", "boil", "mixer", "blender", "toaster", "chop", "whisk", "ladle", "grate", "cut", "slice", "pour", "simmer", "saute", "roast", "broil", "measure", "taste", "sieve", "drain", "spice", "kettle", "timer", "apron", "utensil", "napkin", "table", "kitchen", "ingredient", "recipe", "food", "meal"]
school_list = ["chatgpt", "book", "pencil", "desk", "chalk", "class", "study", "learn", "math", "science", "history", "art", "music", "teacher", "student", "board", "note", "paper", "write", "read", "quiz", "exam", "grade", "project", "lecture", "lesson", "college", "university", "lab", "textbook", "assignment", "homework", "research", "test", "calculator", "marker", "eraser", "backpack", "diagram", "education", "knowledge", "scholar", "question", "answer", "notebook", "highlight", "classroom"]
sports_list = ["ball", "golf", "tennis", "hockey", "soccer", "cricket", "rugby", "swim", "run", "jump", "throw", "catch", "goal", "team", "coach", "player", "match", "court", "field", "gym", "stadium", "race", "bat", "glove", "club", "rink", "net", "racket", "driver", "par", "birdie", "eagle", "putt", "serve", "ace", "strike", "dive", "kick", "pass", "block", "tackle", "sprint", "dribble", "shoot", "score", "win", "lose"]
camping_list = ["tent", "fire", "rope", "map", "hike", "camp", "sleep", "outdoor", "nature", "backpack", "trail", "cook", "forest", "mountain", "lake", "river", "campfire", "flashlight", "compass", "binoculars", "adventure", "wild", "wildlife", "explore", "campsite", "stove", "lantern", "sleeping", "bag", "hiking", "trek", "adventure", "exploration", "firewood", "outdoor", "wilderness", "marshmallow", "tent", "hammock", "campground", "nature", "cooler", "smores", "picnic", "hiker", "trailblazer"]
literature_list = ["novel", "poetry", "drama", "prose", "essay", "fiction", "story", "book", "author", "poet", "play", "verse", "plot", "character", "theme", "genre", "literary", "language", "symbol", "narrative", "metaphor", "rhyme", "stanza", "imagery", "dialogue", "monologue", "soliloquy", "prologue", "epilogue", "chapter", "novella", "classic", "tragedy", "comedy", "satire", "fantasy", "mystery", "adventure", "science", "biography", "autobiography", "critic", "library", "reader", "text"]
music_list = ["song", "guitar", "drums", "piano", "violin", "flute", "trumpet", "saxophone", "singer", "musician", "band", "album", "melody", "harmony", "rhythm", "beat", "note", "chord", "lyrics", "solo", "duet", "concert", "symphony", "opera", "acoustic", "electric", "genre", "classical", "rock", "pop", "jazz", "blues", "country", "hiphop", "rap", "reggae", "folk", "indie", "ballad", "instrument", "studio", "producer", "audience", "stage", "performance", "tour", "radio", "stream", "tenor", "quads", "snare", "bass"]
flowers_list = ["rose", "tulip", "daisy", "lily", "iris", "orchid", "sunflower", "daffodil", "carnation", "poppy", "dandelion", "lavender", "jasmine", "peony", "marigold", "violet", "chrysanthemum", "hibiscus", "lotus", "dahlia", "hydrangea", "cactus", "aster", "bluebell", "buttercup", "crocus", "daisy", "geranium", "gerbera", "honeysuckle", "magnolia", "morning", "glory", "narcissus", "pansy", "petunia", "primrose", "snapdragon", "sunflower", "tulip", "zinnia", "blossom", "botany", "floral", "garden"]

#LIST OF LISTS
categories = ["Technology", "Transportation", "Kitchen", "School", "Sports", "Camping", "Literature", "Music", "Flowers"]

#STICKY NOTE
#password: hangman
sticky_note = " ___________\n|           |\n| password: |\n|  hangman  |\n|___________|\n"
print(sticky_note)
#PASSWORD CODE 
'''password loop to make sure user is user'''
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
print("Welcome User.")

#DEFINGING LEADERBOARD
def leaderboard(name_list, time_taken, strike_count_list, category_list, word_list):
    #LEADERBOARD LISTS
    for i in range(len(name_list)):
        print(f"Name: {name_list[i]}\tTime: {time_taken[i]}\tStrike Count: {strike_count_list[i]}\tCategory: {category_list[i]}\tWord: {word_list[i]}")
    
#DEFINGING GET WORD
def get_rand_word(words):
    return(random.choice(words))

#DEFINING DISPLAY WORD
def display_word(hangman_correct_word, guessed_letter):
    display_word = ""
    for letter in hangman_correct_word:
        if letter in guessed_letter:
            display_word += letter.upper()
        else:
                display_word += "*"
    print(display_word)
    return(display_word)

#DEFINING THE HANGMAN GAME
def play_hangman():
    
    #MAKING THE LISTS GLOBAL 
    global name_list
    global time_taken
    global strike_count_list
    global category_list
    global word_list
    
    #NAME IS NOW GLOBAL 
    global name
    
    #ASSIGNING AREYOUREALLY 
    areyoureally = False
    
    #SKIPPING GAME INTRO IF THE USER IS THE SAME AS BEFORE
    if len(name_list) == 0:
        #INTRO TO GAME
        name = input("\nHello User, Welcome to Hangman.\nEnter your username: ")
        name_list.append(name)
        print(f"Welcome, {name}")
        user_choice = input("\nBefore we start, Would you like a reminder of the rules? [Y/N]: ")
        if user_choice.lower().startswith("y"):
            print("I will think of a word and the you will try to guess it by guessing letters. Each incorrect guess brings you closer to being \"hanged.\". You get 6 incorrect guesses before you get \"hanged\".\n") 
        elif user_choice.lower().startswith("n"):
            print("We will pass this then.\n")
        else:
            print("That\'s not a Yes or a No, So we will continue.\n")
    else:
        while areyoureally == False:
            if whoareyou.upper().startswith("Y"):
                areyoureally = True
            elif whoareyou.upper().startswith("N"):
                #INTRO TO GAME
                name = input("\nHello User, Welcome to Hangman.\nEnter your username: ")
                name_list.append(name)
                print(f"Welcome, {name}")
                user_choice = input("\nBefore we start, Would you like a reminder of the rules? [Y/N]: ")
                if user_choice.lower().startswith("y"):
                    print("I will think of a word and the you will try to guess it by guessing letters. Each incorrect guess brings you closer to being \"hanged.\". You get 6 incorrect guesses before you get \"hanged\".\n") 
                    areyoureally = True
                elif user_choice.lower().startswith("n"):
                    print("We will pass this then")
                    areyoureally = True
                else:
                    print("That\'s not a Yes or a No, So we will continue.\n")
                    areyoureally = True
            else:
                areyoureally = False

    #TIME FOR PARRAL LISTS
    timestart = time.time()

    #SELECTING LISTS
    words = {"Technology": technology_list, "Transportation": transportation_list, "Kitchen": kitchen_list, "School": school_list, "Sports": sports_list, "Camping": camping_list, "Literature": literature_list, "Music": music_list, "Flowers": flowers_list}
    category = random.choice(categories)
    the_words = words[category]

    #RANDOM INDEX FROM THE LISTS
    random_num = random.randint(0,(len(the_words) - 1))

    #SELECTING THE RANDOM WORD FROM THE SELECTED LIST
    hangman_correct_word = get_rand_word(the_words).upper()
    word_list.append(hangman_correct_word)

    #TELLING THE USER THEIR SELECTED LIST
    print("Your category is", category)
    category_list.append(category)
    
    #USERINPUT OF WORD
    try:
        user_guess = input("\nAlright, Lets start.\nWhat is your first guess? ")
    except TypeError: 
        pass
    
    #STICK FIGURE
    #note stick figure list index is 0 - 6
    stick_figure_list = ["" , "  0\n" , "  0\n  I\n" , "  0\n /I\n" , "  0\n /I\\\n" , "  0\n /I\\\n /\n" , "  0\n /I\\\n / \\\n"]
    stick_figure_strike_count = 0
    #LISTS FOR PARRAL LIST
    
    #GUESSED LETTERS
    guessed_letter = ""
    
    #HANGMAN GAME
    while user_guess.upper().isalpha() and len(user_guess) == int("1"):
        if user_guess.upper() in hangman_correct_word and user_guess.upper() not in guessed_letter:
            guessed_letter = guessed_letter + user_guess.upper()
            print(stick_figure_list[stick_figure_strike_count])
            displayed_word = display_word(hangman_correct_word, guessed_letter)
            if displayed_word == hangman_correct_word:
                print(stick_figure_list[stick_figure_strike_count])
                print("You Win!")
                timeend = time.time()
                time_taken_math = timeend - timestart
                time_taken.append(str(time_taken_math))
                strike_count_list.append(str(stick_figure_strike_count))
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
                timeend = time.time()
                time_taken_math = timeend - timestart
                time_taken.append(str(time_taken_math))
                strike_count_list.append(str(stick_figure_strike_count))
                break
            else:
                pass
            user_guess = input("Next Guess? ")
    if len(user_guess) > 1:
        print("!CHEATER!\n!1 LETTER AT A TIME!")
        stick_figure_strike_count = "CHEATER"
        timeend = time.time()
        time_taken_math = timeend - timestart
        time_taken.append(str(time_taken_math))
        strike_count_list.append(stick_figure_strike_count)
    elif user_guess == " ":
        print("!ERROR!\n!PLEASE PRINT EITHER A LETTER OR A SPACE!")
        stick_figure_strike_count = "ERROR"
        timeend = time.time()
        time_taken_math = timeend - timestart
        time_taken.append(str(time_taken_math))
        strike_count_list.append(str(stick_figure_strike_count))
    else:
        pass
    
#GAME LOOP
while True:
    play_hangman()
    leaderboard(name_list, time_taken, strike_count_list, category_list, word_list)
    playagain = input("\nWould you like to play play again [Y/N]: ")
    if playagain.upper() == "N":
        print("\nThank You for Playing!")
        print("\n|\n \\ 0\n   M \\\n   V  |\n  / \\\n |   |\n")
        break
    else:
        whoareyou = input(f"Are you {name}? [Y/N]: ")
        print()
        continue
