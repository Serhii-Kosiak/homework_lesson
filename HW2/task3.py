# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name.
# Find those who are on all blacklists.

casino_blacklist = {'Name Ace', 'Name King', 'Name Queen', 'Name Ten'}
poker_blacklist = {'Name Joker', 'Name Ace', 'Name King', 'Name 5', 'Name 6', 'Name 7'}
alcohol_blacklist = {'Name 9', 'Name 10', 'Name Ace', 'Name 12', 'Name King'}

result = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(result)
