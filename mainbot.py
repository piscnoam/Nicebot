import assistantbot
import calcubot
import gamebot
import goalbot

def robo():
    roboChoice = input("\nWhat function do you need today?(Enter any of the following: games, goals, calculating, assistance)\n")
    if roboChoice.lower() == 'games':
        gamebot.main()
    elif roboChoice.lower() == 'goals':
        goalbot.main()
    elif roboChoice.lower() == 'calculating':
        calcubot.main()
    elif roboChoice.lower() == 'assistance':
        assistantbot.main()

if __name__ == "__main__":
    robo()
