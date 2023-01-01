import os, inquirer

def getPlayerBalance(username):
  os.system('cls')

  choices = [10000, 15000]

  questions = [
    inquirer.List(
      'balance',
      message = f'{username}, select your balance',
      choices = [f'{i} chips' for i in choices],
      carousel = True
    )
  ]

  return inquirer.prompt(questions)['balance']

def getPlayerBet(player):
  os.system('cls')

  choices = filter(lambda item: item <= player.balance, [100, 500, 1000])

  questions = [
    inquirer.List(
      'bet',
      message = f'{player.username}, you have {player.balance} chips. Make your bet',
      choices = [f'{i} chips' for i in choices],
      carousel = True
    )
  ]

  return inquirer.prompt(questions)['bet']

def getPlayerChoice(player):
  choices = ['Stand', 'Hit']
  
  if player.isDoublePossible:
    choices.append('DoubleDown')

  if player.isSplitPossible:
    choices.append('Split')

  questions = [
    inquirer.List('action', message = 'Select action', choices = choices, carousel = True)
  ]

  return inquirer.prompt(questions)['action']