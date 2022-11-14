## The script of the game goes in this file.
##
# Declare characters used by this game. The color argument colorizes the
# name of the character.
##
define eil = Character("Eileen")
define user = Character("User")
define ops = Character("Operator")
##
# The game starts here.
##
## label start is always going to be the beginning of the game. 
label start:
    $ username = renpy.input('Enter username')
    show screen cmd_screen
    
    return
##