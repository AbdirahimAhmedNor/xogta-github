def get_longest_streak(contributions):

  longest_streak = 0
  count = 0

  for i, weeks in enumerate(contributions['contributions']):
    for index, week in enumerate(weeks):
      if week['contributionCount'] > 0:
        count += 1
      else:
        if count > longest_streak:
          longest_streak = count
        count = 0

  return longest_streak

