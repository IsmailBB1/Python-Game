import random

list = ["stone","scissors","paper"]
print ("Game rules:", "Stone crushes scissors, paper covers the stone and scissors cut the paper.")
while True:
    print ("stone","scissors","paper")
    choice = input ("Select one:")
    answer = random.choice(list) 
    print ("The other player's answer:", answer)
    if choice == list[0] and answer == list [1]:
     print ("Congratulations, you won the game")
     if choice == list [1] and answer == list [2]:
      print ("Congratulations, you won the game")
      if choice == list[2] and answer == list [0]:
       print ("Congratulations, you won the game")
    elif choice == answer:
     print ("Draw")
    else :
     print ("You've lost")
    print ("Would you like to play again? (Y/N)")
    karar = input ("Your decision:")
    if karar == "Y":
     continue  
    else:
       break      