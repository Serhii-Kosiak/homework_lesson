# you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format  ["first_item", "friends_list", "my_tuple"]

camelcase = ["FirstItem", "FriendsList", "MyTuple"]
lowercase = []

for element in camelcase:
    element = element[0].lower() + element[1:]

    for i in element:
        if i.isupper():
            element = element.replace(i, f"_{i.lower()}")
    lowercase.append(element)

print(lowercase)
