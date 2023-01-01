from participant import Participant
from deck import Deck
from .dealerActions import DealerActions

class Dealer(Participant):
  def __init__(self):
    super().__init__()

    self.__cards = Deck().cards
    self.actions = DealerActions(self, self.__cards)

  def printHand(self):
    print(f'Dealer cards: {self.cards} ({self.score})')