# You have a group of people with non-unique names. Generate a list of non-duplicate names
# (you cannot use set for this task. If there are 2 johns in the list, you need to take only one of them.
# "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

names_list = ["John Dow", "John Dow", "Marta Dow", "Liam Smith", "Liam Smith", "John Doe", "John Doe"]

unique_names_list = []

for name in names_list:
    if name not in unique_names_list:
        unique_names_list.append(name)

print(unique_names_list)
