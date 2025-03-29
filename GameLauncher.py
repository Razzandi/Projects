import sys


title_screen = input("Welcome to my games! If you would like to play, type 'play', and if you would like to quit, type 'quit' >").lower()

print(title_screen)
if title_screen == "play": 
    games_menu = ["Rock, Paper, Scissors", "Number Guesser", "Quiz Game", "Space Invaders", "Adventure"]
    print(games_menu)
    game_selection = input("Please enter the name of which game you'd like to play! >").lower()
    print(game_selection)
    if game_selection == "rock, paper, scissors":
        import RockPaperScissors
    elif game_selection == "number guesser":
        import NumberGuesser
    elif game_selection == "quiz game":
        import QuizGame
    elif game_selection == "space invaders":
        import SpaceInvaders
    elif game_selection == "adventure":
        import AdventureGame
    else:
        print(game_selection)








else:
    quit()