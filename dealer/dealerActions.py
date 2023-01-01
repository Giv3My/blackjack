import os, time, random

class DealerActions():
  def __init__(self, dealer, cards):
    self.__dealer = dealer
    self.__cards = cards

  def __shuffleCards(self):
    random.shuffle(self.__cards)

  def getCard(self):
    time.sleep(1)

    return self.__cards.pop()

  def hit(self, isHidden = False):
    card = self.getCard()
    self.__dealer.hand.append(card)

    print(f'Dealer got: {card}\n') if not isHidden else print(f'Dealer got: [X]')

  def dealCards(self, players):
    os.system('cls')
    print('Dealing cards...\n')

    self.__shuffleCards()

    for i in range(2):
      for player in players:
        player.actions.hit(self.__dealer)

      isHidden = False if (i < 1) else True

      self.__dealer.actions.hit(isHidden)