A simple implementation of the mini-max algorith in python in terms of tic tac toe
# The mini max algorithm
## Simple overview
The mini max algorithm is a recursive algorithm that calculates the best moves by calculating a tree of possibilities and determening which one is better by recursivly repeating the algorithm until reaching a *terminal position* (or in more complicated stuff like chess a specific depth)
<br> It is best used when there are 2 players each with opposing goals and only one winner <br>
one of the player is called the MAX player (X in our case) and the other is MIN (O), when calling the minimax function the max player will want to *maximize* the value and the min to *minimize*
# Implementation
We have 4 main functions (one of which is two):
## Terminal and state
Terminal determins whether the specific position is a terminal position or not <br>
state determins which one is it (-1 if the min player won, 1 if the max, 0 if draw)
## Action
It gives all of the possible moves from a specific position, in tic tac toe it's super simple, however it can get very complicated)
## Result
Result will compute the result of a specific action.
## Minimax
Minimax will recursivly call it self for each action each time on the other player until reaching a terminal position at which point it'll calculate what's the best route to go to.

