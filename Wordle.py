import random

def wordle_test(cw, lifes):
    cl = list(cw)
    wlen = len(cw)
    default_win = "Correct! You won!"
    win = default_win
    eggs = {
        "backwards": "!now uoY !tcerroC",
        "duck": "Quack quack! Youre - quack - right!",
        "robot": "Beep-bop. You are correct."
    }
    print("Hello! This is Pedro's Python Wordle!")
    print("I'll choose a word for you and then you have to guess what it is!")
    print("X means wrong place and letter, A means right letter but wrong")
    print("  place, and R means it's correct!")
    print("Ready? Then let's go!")
    print("The word is " + str(wlen) + " letters long.")
    right = False
    gl = []
    explanation = []
    explanation1 = ""
    for x in range(lifes):
        if right == False:
            explanation = []
            gw = input("What's the word? ")
            if len(gw) != len(cw):
                print(f"What? The word I asked you for was {wlen} letters long!")
                continue
            gl = list(gw)
            for y in range(wlen):
                if gl[y] == cl[y]:
                    explanation.append("R")
                elif gl[y] in cl:
                    explanation.append("A")
                elif gl[y] not in cl:
                    explanation.append("X")
            result = "".join(explanation)
            print(result)
            if gw == cw:
                right = True
                if cw in eggs:
                    win = eggs[cw]
                print(win)

def random_wordle(pws, lifes):
    cw = random.choice(pws)
    wordle_test(cw, lifes)

word_list = ["pedro", "frisk", "rocky", "mulan", "stone", "bread", "mouse", "pikachu", "group", "clean", "toothbrush", "chameleon", "charizard", "wolf", "nose", "hole", "duck", "backwards", "robot"]
word = input("Test Word is: ")
wordle_test(word, 6)
