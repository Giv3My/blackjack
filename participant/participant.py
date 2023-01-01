class Participant:
  @property
  def cards(self):
    return f"[{', '.join(str(card) for card in self.hand)}]"

  @property
  def score(self):
    value = sum(card.value for card in self.hand)
    aces = sum(getattr(card, 'isAce', False) for card in self.hand)

    while value > 21 and aces:
      value -= 10
      aces -= 1

    return value

  @property
  def isBlackjack(self):
    if len(self.hand) == 2 and self.score == 21:
      return True

    return False

  def __init__(self):
    self.hand = []