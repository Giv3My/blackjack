class Card:
  def __init__(self, rank):
    self.rank = rank

    if rank == 'A':
      self.isAce = True
      self.value = 11
    elif rank in ['J', 'Q', 'K']:
      self.value = 10
    else:
      self.value = int(rank)

  def __str__(self):
    return str(self.rank)