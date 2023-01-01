def calculateScore(acc, item):
  if getattr(item, 'altValue', None):
    acc += item.altValue if item.value + acc > 21 else item.value

    return acc

  return acc + item.value