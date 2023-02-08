# Rock-Paper-Scissors

import random

botWin = 0
playerWin = 0
draw = 0

def rps_game():
  playerAnswer = input("\nRock | Paper | Scissors ").lower()

  rpsOptions = ['rock', 'paper', 'scissors']
  botAnswer = random.choice(rpsOptions)
  
  if (playerAnswer == 'rock' or 'paper' or 'scissors'):

    global draw
    global botWin
    global playerWin

    if (botAnswer == playerAnswer):
      print("------------------")
      print('\033[1m' + "\nIt's a Draw!\n" + "\033[0;0m")
      print("Your Answer: " + playerAnswer + "\nBot Answer: " + botAnswer)
      print("------------------\n")
      draw += 1
    elif(botAnswer == 'scissors' and playerAnswer == 'paper'):
      print("------------------")
      print('\033[1m' +  "\nYou lose!\n" + "\033[0;0m")
      print("Your Answer: " + playerAnswer + "\nBot Answer: " + botAnswer)
      print("------------------\n")
      botWin += 1
    elif(botAnswer == 'paper' and playerAnswer == 'rock'):
      print("------------------")
      print('\033[1m' + "\nYou lose!\n" + "\033[0;0m")
      print("Your Answer: " + playerAnswer + "\nBot Answer: " + botAnswer)
      print("------------------\n")
      botWin += 1
    elif(botAnswer == 'rock' and playerAnswer == 'scissors'):
      print("------------------")
      print('\033[1m' + "\nYou lose!\n" + "\033[0;0m")
      print("Your Answer: " + playerAnswer + "\nBot Answer: " + botAnswer)
      print("------------------\n")
      botWin += 1
    else:
      print("------------------")
      print('\033[1m' + "\nYou win!\n" + "\033[0;0m")
      print("Your Answer: " + playerAnswer + "\nBot Answer: " + botAnswer)
      print("------------------\n")
      playerWin += 1
  else:
      print("Invalid input")
      
for i in range(10):
  rps_game()

print("Wins: " + str(playerWin))
print("Losses: " + str(botWin))
print("Draws: " + str(draw))

if (playerWin > botWin):
  print('\033[1m' + "\nYou won!" + "\033[0;0m")
elif (playerWin < botWin):
  print('\033[1m' + "\nYou lost!" + "\033[0;0m")
else:
  print('\033[1m' + "\nIt's a draw!" + "\033[0;0m")