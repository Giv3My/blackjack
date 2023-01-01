import os
from helpers.player import getPlayerBalance
from player import Player

def checkUsernameInList(username, players):
  while username in list(map(lambda p: p.username, players)):
    os.system('cls')
    
    username = input('This username is already exist. Try again: ')

  return username

def getUsername(username, players):
  username = checkUsernameInList(username, players)
  
  while not username.strip():
    os.system('cls')

    username = checkUsernameInList(input('Username can\'t be empty. Try again: '), players)

  return username

def getBalance(username):
  return int(getPlayerBalance(username).split(' ')[0])

def addPlayers(count):
  players = []

  for i in range(count):
    os.system('cls')

    username = getUsername(input(f'Player {i + 1} username: '), players)
    balance = getBalance(username)

    newPlayer = Player(username, balance)
    players.append(newPlayer)
  
  return players