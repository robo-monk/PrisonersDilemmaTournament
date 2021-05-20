import numpy as np
import random

'''
Base Idea:
Whatever our algorythm becomes, it's going to inherently affect it's future input, since the output will probably affect the future's input.
It's a recursive paradise. I'm in the middle of a very heavy exam week -not doing great- and instead chose to actively invest my time into this. Thanks cary :)

My naive brain wants to make an algorythm that when it runs against itself, it should win 50% of the times. In every other case, it should completely obliterate the opponent.

Memento from the really nice Christopher Nolan movie.
'''

'''
Memory formation:

[
   [1, 0, 1], # list with our choices so far
   [0, 1, 1], # list with their choices so far
]

'''

def strategy(history, memory):
    return 1, None

