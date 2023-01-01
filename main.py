import os
from game import Game
from helpers.game import getGameStatus, getPlayersCount 

gameStatus = True if getGameStatus('Do you wanna play BlackJack?') else False

if gameStatus:
  maxPlayersCount = 3

  count = int(getPlayersCount(maxPlayersCount))

  game = Game(count)
  game.start()

  while game.canContinue and gameStatus:
    if getGameStatus('Wanna try again?'):
      game.restart()
    else:
      gameStatus = False

os.system('cls')