#choose your own adventure



answer = input("You've been walking on a dirt road for what seems like hours, with no other person in sight. On either side of you are trees, and the sounds of a river in the distance. You reach a dead end, with a choice to make.. Do you go back? Or press forward? (Back/Forward) ")
if answer.lower() == "forward":
    answer = input("You press forward, with no intentions of going back the way you came, walking through the trees that loom over you with intimidating height, a while passes until you come across a river. There's a wobbly bridge that crosses it, with no other way around.. Do you cross the bridge? or swim across? (Bridge/Swim) ")
    if answer.lower() == "bridge":
        print("You walk across the bridge, the wood creaking and groaning under your weight, you make it halfway over the bridge, when you hear a loud snap. The world seems to pull you towards it, and you feel a rush of warmth, a sharp pain in your chest. You were impaled.")
        print("Game Over - you were impaled by a broken wooden board")
    elif answer.lower() == "swim":
        print("You choose to swim across the river. You enter the river, wading through the water, slowly making your way across. The water was cold enough to chill you to your very core.. Your next step didn't find the river floor, and now you've started to swim. You're almost halfway across the river when you hear a loud snap. You look around quickly to see what made the noise, but the only thing you see is a tree... falling... oh so slowly.. ontop of you")
        print("Game Over - you were crushed by a tree")
elif answer.lower() == "back":
    print(("You turn back and begin to walk down the road you just travelled.."
   "  Getting lost in the woods seems like a much worse option. Soon enough you"
   " see a car drive by -- You wave it down and are taken to the nearest police"
   " station for help."))
    print("You win!")
    print("Thank you for playing")
    



