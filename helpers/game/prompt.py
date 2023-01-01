import os, inquirer
from inquirer.themes import GreenPassion

def getGameStatus(message):
  os.system('cls')

  questions = [
    inquirer.Confirm('gameStatus', message = message, default = True),
  ] 

  return inquirer.prompt(questions, theme = GreenPassion())['gameStatus']

def getPlayersCount(maxCount):
  os.system('cls')

  choices = [i + 1 for i in range(maxCount)]

  questions = [
    inquirer.List('count', message = 'Select count of players', choices = choices, carousel = True)
  ]

  return inquirer.prompt(questions)['count']