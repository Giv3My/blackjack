def checkWin(player, dealer = None):
  if not dealer:
    if player.score > 21:
      player.isBust = True

      print(f'{player.username} lose.')
  else:
    if player.isBlackjack and not dealer.isBlackjack:
      player.totalWin += player.totalBet * 2.5
      
      print(f'{player.username} win with Blackjack {player.totalWin} chips')
    elif dealer.score > 21 or player.score > dealer.score:
      player.totalWin += player.totalBet * 2

      print(f'{player.username} win {player.totalWin} chips')
    elif player.score == dealer.score:
      player.totalWin += player.totalBet

      print(f'{player.username} has a push this time.')
    else:
      player.isBust = True

      print(f'{player.username} lose.')