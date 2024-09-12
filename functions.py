# functions -- block of code that does nothing UNTIL called upon
# used for epetitive actions- can be called upon whenever needed
# DRY :don't repeat yourself !!

# "def" notifiees the code that the function is about to start
# my_function is the name of the function, the parenthesees are
# for the perameters (code below has none). ":" lets code know that 
# the next block of code is part of the function
def my_function():
    print("oopsies")

# anything indented is part of the function
# you have to call the code to run itby writing the name of the function
#  in parenthesees (not indented)


def npc_greeting():
    print("why are we still  here. just to suffer")

npc_greeting()

# parameters allows functions to accept data as an input value
def player_response(player_response):
    print(player_response)

answer_no = "no thanks"
answer_yes = "yessssss shawty"
player_response(answer_no)
player_response(answer_yes)

npc_greeting()
npc_greeting(answer_yes)

def approach_vendor():
    npc_greeting()
    player_response = input("1 for yes, 2 for no")
    player_response = int(player_response)

    if (player_response == 1):
        print("i want to buy mr pipe")
    elif (player_response == 2):
        print("player vanishes like my dad 11 years ago")
    else:
        print("what are you saying to me?.... give me burger")

approach_vendor()