from .card import Card

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Deck:
  @property
  def cards(self):
    return self.__cards

  def __init__(self):
    self.__cards = [Card(rank) for _ in range(4) for rank in ranks]