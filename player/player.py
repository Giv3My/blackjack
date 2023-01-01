from functools import reduce
from participant import Participant
from .playerActions import PlayerActions

class Player(Participant):
  @property
  def isSplitPossible(self):
    if self.balance < self.totalBet or len(self.hand) > 2 or self.isSplit:
      return False

    return all(self.hand[i].value == self.hand[i + 1].value for i in range(len(self.hand) - 1))

  @property
  def isDoublePossible(self):
    if self.balance < self.totalBet or len(self.hand) > 2 or self.isSplit:
      return False
    
    return True

  @property
  def totalWin(self):
    if self.split:
      return reduce(lambda acc, s: acc + s.totalWin, self.split, 0)

    return self.__totalWin
  
  @totalWin.setter
  def totalWin(self, value):
    self.__totalWin = int(value)

  @property
  def balance(self):
    self.__balance += self.totalWin

    return self.__balance

  @balance.setter
  def balance(self, value):
    self.__balance = value

  def __init__(self, username, balance = 0):
    super().__init__()

    self.username = username
    self.__balance = balance
    self.split = []
    self.totalBet = 0
    self.__totalWin = 0
    self.isSplit = False
    self.isBust = False
    self.actions = PlayerActions(self)

  def resetPlayerInfo(self):
    self.hand = []
    self.split = []
    self.totalBet = 0
    self.__totalWin = 0
    self.isSplit = False
    self.isBust = False

    return self

  def printHand(self):
    print(f'{self.username}, your cards: {self.cards} ({self.score})')

  def printBalance(self):
    if self.totalWin > 0:
      print(f'{self.username}, you have {self.balance} chips (+{self.totalWin})')
    else:
      print(f'{self.username}, you have {self.balance} chips (-{self.totalBet})')