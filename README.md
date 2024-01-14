# PyWordle
I discovered how to make a wordle-like game using python, and PyWordle is what I made.

I want you to put new words here, and... I actually want easter eggs that are shown after you win with a certain word.

## Test Example:
```
>>> import Wordle
>>> Wordle.random_wordle(Wordle.word_list, 10)
Hello! This is Pedro's Python Wordle!
I'll choose a word for you and then you have to guess what it is!
X means wrong place and letter, A means right letter but wrong
  place, and R means it's correct!
Ready? Then let's go!
The word is 5 letters long.
What's the word? pedro
XAAAX
What's the word? stone
XXXXA
What's the word? bread
RRRRR
Correct! You won!
>>>
```

## Easter Egg Example:
```
Hello! This is Pedro's Python Wordle!
I'll choose a word for you and then you have to guess what it is!
X means wrong place and letter, A means right letter but wrong
  place, and R means it's correct!
Ready? Then let's go!
The word is 5 letters long.
What's the word? robot
RRRRR
Beep-bop. You are correct.
```
