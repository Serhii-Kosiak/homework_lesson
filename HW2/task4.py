# You have two groups of people. One group consists of omnivores, the other only vegetarians.
# An omnivore is a vegetarian but a vegetarian is not an omnivore.
# Display a list of guests who can eat vegetables and herbs.

Omnivores = ['People1', 'People2', 'People3', 'People4']
Vegeterians = ['Vege1', 'Vege2', 'Vege3', 'Vege4']

Omnivores.extend(Vegeterians)
print(Omnivores)
