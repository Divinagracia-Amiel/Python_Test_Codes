import time
import random

load_between_actions = 0.5
maximum_value = 100
dice_face = 6

snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

player_turns = [
    "Your turn na mamshie.",
    "Gow gow gooow!.",
    "Go lang nang go.",
    "Para sa'yo ang laban na 'to.",
    "Kapitbahay! Handa na ba kayo?!",
    "",
]

snake_bite_text = [
    "Awit, Nag-aral ka ba?",
    "More Review pa, bro!",
    "Ay. Naahas.",
    "Boom. Inahas!",
    "Pati ahas, high-tech na!"
]

ladder_jump_text = [
    "Wow. Naka-chamba rin.",
    "Wow. Prepared. Nag-aral.",
    "WEh? Alam mo ba talaga sagot sa tanong na yun?",
    "Einstein, is that you?!",
    "Sana grades mo rin tumaas."
]


question = {1:"Who is the first president of the United States ",   
            2:"What were the first ever civilization in the world ",
            3:"Who came up with the formula E=mc^2? ",
            4:"Who is the father of modern mathematics? ",
            5:"What country provoked the US in joining the World War II? ",
            6:"What is the highest number used in a Sudoku puzzle? ",
            7:"3 + 25 – 16 x 3 ÷ 2? ",
            8:"What is the acceleration constant of gravity? ",
            9:"What is the term for a positive electrode? ",
            10:"Which cities of japan did US dropped the atomic bomb? ",
            11:"Which swimming stroke is named after an insect? ",
            12:"What is the powerhouse of the cell? ",
            13:"How to expand perfect square binomial? ",
            14:"What number is “dos” in Spanish? ",
            15:"What theory did Nicolas Copernicus came up about the solar system? ",
            16:"Negative divided by positive is equals to? ",
            17:"The moon landing was one of the greatest achievements of mankind. What year did it occur? ",
            18:"Which is the first month of the year to have exactly 30 days? ",
            19:"Most living things are made up out of what? ",
            20:"105 – 60 + 2? ",
            21:"Which two main countries were involved in the Cold War? ",
            22:"What is the weakest mineral in the Mohs Scale? ",
            23:"Whose ship was the first to sail around the world? ",
            24:"What is the 55% of 450? ",
            25:"What is the highest frequency of the electromagnetic spectrum? ",
            26:"How many years did Spain colonize the Philippines? ",
            27:"5! ",
            28:"What currency is used in South Korea? "}

choices = {1:"a.) George Washington\nb.) Thomas Jefferson\nc.) John Adams\nd.) Abraham Lincoln",
           2:"a.) Egyptians\nb.) Mayans\nc.) Yakshas\nd.) Mesopotamia",
           3:"a.) Albert Einstein\nb.) Earnest Rutherford\nc.) Marie Curie\nd.) Erwin Schrodinger",
           4:"a.) Euclid\nb.) Rene Descartes\nc.) Claudius Ptolemy\nd.) John Napier",
           5:"a.) Japan\nb.) Germany\nc.) Russia\nd.) Britain",
           6:"a.) 8\nb.) 7\nc.) 9\nd.) 6",
           7:"a.) 9\nb.) 18\nc.) 4\nd.) 15",
           8:"a.) 10 m/s^2\nb.) 9.8 m/s^2\nc.) 10 m/s\nd.) 9.8 m/s",
           9:"a.) Anode\nb.) Cathode\nc.) Cation\nd.) Anion",
           10:"a.) Tokyo and Osaka\nb.) Kyoto and Hiroshima\nc.) Nagasaki and Hiroshima\nd.) Osaka and Nagasaki",
           11:"a.) dragonfly\nb.) ladybug\nc.) grasshopper\nd.) butterfly",
           12:"a.) Nucleus\nb.) Cytoplasm\nc.) Mitochondria\nd.) Golgi Apparatus",
           13:"a.) Square the first term, twice the product of two terms, square the last term.\nb.) Square the first term, get the product of two terms, square the last term.\nc.) Square the first term, perform the operation of two terms, square the last term.\nd.) Square the first term, half the product of two terms, square the last term.",
           14:"a.) 4\nb.) 2\nc.) 3\nd.) 5",
           15:"a.) Theory of Relativity\nb.) Geocentric Theory\nc.) String Theory\nd.) Heliocentric Theory",
           16:"a.) Positive\nb.) Copy the sign of the larger number.\nc.) positive or negative(+-)\nd.) Negative",
           17:"a.) 1968\nb.) 1969\nc.) 1970\nd.) 1971",
           18:"a.) April\nb.) March\nc.) May\nd.) June",
           19:"a.) Carbon\nb.) Hydrogen\nc.) Nitrogen\nd.) Oxygen",
           20:"a.) 45\nb.) 43\nc.) -43\nd.) 47",
           21:"a.) US and China\nb.) Britain and Russia\nc.) Germany and France\nd.) US and Russia",
           22:"a.) Diamond\nb.) Talc\nc.) Corundum\nd.) Gypsum",
           23:"a.) Cristopher Columbus\nb.) Napoleon Bonaparte\nc.) Ferdinand Magellan\nd.) Marco Polo",
           24:"a.) 245Euclid\nb.) 247.5\nc.) 230.5\nd.) 252.5",
           25:"a.) Radio waves\nb.) X-rays\nc.) Gamma rays\nd.) Infrared",
           26:"a.) 331\nb.) 332\nc.) 333\nd.) 334",
           27:"a.) 120\nb.) 250\nc.) 3125\nd.) 5",
           28:"a.) Yen\nb.) Krone\nc.) Won\nd.) Euro"}

answer_key = {1:'a',
              2:'d',
              3:'a',
              4:'b',
              5:'a',
              6:'c',
              7:'c',
              8:'b',
              9:'b',
              10:'c',
              11:'d',
              12:'c',
              13:'a',
              14:'b',
              15:'d',
              16:'d',
              17:'b',
              18:'a',
              19:'a',
              20:'d',
              21:'d',
              22:'b',
              23:'c',
              24:'b',
              25:'c',
              26:'c',
              27:'a',
              28:'c'}


def intro_and_rules():
    msg = """
    Welcome to the Modified Snakes and Ladders Game.
    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you land at the bottom of a ladder, you will be given a question and if you answer it correctly, you can move up to the top of the ladder. If not, you cannot move up to the top of the ladder.
      3. If you land on the head of a snake, you will be given a question and if you answer it correctly, you can continue without going to the bottom of the snake. If not, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
    
    """
    print(msg)


def player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def dice_value():
    time.sleep(load_between_actions)
    dice_value = random.randint(1, dice_face)
    print("Its a " + str(dice_value))
    return dice_value

def randomy():
    from random import randint
    ran_qanda = randint(1,28)
    return ran_qanda


def answer_check(answer, key):
    if answer.lower().strip() != answer_key.get(key):
        correct = 0
        return correct
    else:
        correct = 1
        return correct


def got_snake_bite_text(old_value, current_value, player_name):
    print("Mali ka don, mars!\n")
    print("\n" + random.choice(snake_bite_text).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))
    return current_value


def got_ladder_jump_text(old_value, current_value, player_name):
    print("Yes naman!!\n")
    print("\n" + random.choice(ladder_jump_text).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))
    return current_value


def got_incorrect_answer_ladder(old_value, current_value, player_name):
    print("Engk! Wrong choice ka, beshy!\n")
    print("\n" + player_name + " you can't go up to the ladder. You are still at " + str(current_value))
    return current_value


def got_correct_answer_snake(old_value, current_value, player_name):
    print("Ting! Ting! Ting! May tama ka!\n")
    print("\n" + player_name + " you will not slide down the snake. You are still at " + str(current_value))
    return current_value


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(load_between_actions)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > maximum_value:
        print("You need " + str(maximum_value - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        key = randomy()
        print("You got bitten by a snake")
        print(question.get(key))
        print(choices.get(key))
        while True:
            try:               
                answer = input(str("What is the answer? "))
                break
            except ValueError:
                print("Please enter a letter")
                continue
        correct = answer_check(answer, key)
        if correct == 0:
            final_value = snakes.get(current_value)
            current_value = got_snake_bite_text(current_value, final_value, player_name)
        else:
            final_value = current_value
            current_value = got_correct_answer_snake(current_value, final_value, player_name)

    elif current_value in ladders:
        key = randomy()
        print("You hit a ladder")
        print(question.get(key))
        print(choices.get(key))
        while True:
            try:                
                answer = input("What is the answer? ")
                break
            except ValueError:
                print("Please enter a letter")
                continue
        correct = answer_check(answer, key)
        if correct == 1:
            final_value = ladders.get(current_value)
            current_value = got_ladder_jump_text(current_value, final_value, player_name)
        else:
            final_value = current_value
            current_value = got_incorrect_answer_ladder(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(load_between_actions)
    if maximum_value == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        while True:
            again = int(input("Do you want to play again? (1/0): "))
            if again == 1:
                starty()

            elif again == 0:
                print("See you again")
                break

            else:
                print("You have entered a wrong value, please try again")
                continue

def starty():
    intro_and_rules()
    time.sleep(load_between_actions)
    player1_name, player2_name = player_names()
    time.sleep(load_between_actions)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(load_between_actions)
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turns) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(load_between_actions)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turns) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(load_between_actions)
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    starty()