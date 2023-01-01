import player.player as p

class PlayerActions():
  def __init__(self, player):
    self.__player = player

  def bet(self, bet):
    self.__player.totalBet += bet
    self.__player.balance -= bet

    print(f'{self.__player.username}, you have: {self.__player.balance} chips (-{bet})')

  def hit(self, dealer):
    card = dealer.actions.getCard()
    self.__player.hand.append(card)

    print(f'{self.__player.username} got: {card.rank}')

  def split(self, dealer):
    print('Splitting...\n')

    self.bet(self.__player.totalBet)

    self.__player.split = [
      p.Player(f'{self.__player.username} split #1'),
      p.Player(f'{self.__player.username} split #2')
    ]

    for i, splittedPlayer in enumerate(self.__player.split):
      splittedPlayer.isSplit = True
      splittedPlayer.totalBet = self.__player.totalBet / 2

      splittedPlayer.hand.append(self.__player.hand[i])
      splittedPlayer.actions.hit(dealer)

  def doubleDown(self, dealer):
    self.bet(self.__player.totalBet)

    self.hit(dealer)