import os
from dealer import Dealer
from helpers import pressAnyKey
from helpers.game import addPlayers
from helpers.player import getPlayerBet, getPlayerChoice
from helpers.participant import checkWin

class Game:
  @property
  def players(self):
    result = []

    for player in self.__players:
      if len(player.split):
        result += player.split
      else:
        result.append(player)

    return result

  @property
  def canContinue(self):
    return bool(self.__players)

  def __init__(self, count):
    self.__players = addPlayers(count)
    self.__minBet = 100
   
  def __makeBets(self):
    for player in self.players:
      if player.balance < self.__minBet:
        self.__players = list(filter(lambda p: p.balance > self.__minBet, self.__players))

        print(f'{player.username}, your balance is less then min bet ({player.balance})')

        pressAnyKey()
        
        continue

      bet = int(getPlayerBet(player).split(' ')[0])
      player.actions.bet(bet)

      pressAnyKey()

  def __play(self, player, dealer):
    player.printHand()

    if player.isBlackjack:
      pressAnyKey()
      
    while player.score < 21:
      answer = getPlayerChoice(player)

      if answer == 'Hit':
        player.actions.hit(dealer)
        player.printHand()

        checkWin(player)

        if player.isBust or player.score == 21:
          pressAnyKey()
          
          break
      else:
        if answer == 'Stand':
          break

        if answer == 'DoubleDown':
          player.actions.doubleDown(dealer)
          player.printHand()

          checkWin(player)

          pressAnyKey()
          
        if answer == 'Split':
          os.system('cls')

          player.actions.split(dealer)

          pressAnyKey()
          
          for splittedPlayer in player.split:
            os.system('cls')

            self.__play(splittedPlayer, dealer)

        break
       
  def start(self):
    os.system('cls')

    self.__makeBets()
      
    if not self.canContinue:
      return

    dealer = Dealer()
    dealer.actions.dealCards(self.__players)

    pressAnyKey()
    
    for player in self.__players:
      os.system('cls')

      self.__play(player, dealer)

    remainingPlayers = list(filter(lambda p: p.isBust == False, self.players))

    os.system('cls')

    if dealer.score < 17 and len(remainingPlayers):
      dealer.printHand()

      while dealer.score < 17:
        dealer.actions.hit()

    dealer.printHand()

    for player in remainingPlayers:
      checkWin(player, dealer)

    self.__printPlayersBalance()

  def restart(self):
    self.__players = list(map(lambda p: p.resetPlayerInfo(), self.__players))

    self.start()

  def __printPlayersBalance(self):
    print('\nPlayers balance:')

    for player in self.__players:
      player.printBalance()

    pressAnyKey()