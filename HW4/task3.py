# there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}

somelist = 'name=Amanda=sssss&age=32&&salary=1500&currency=euro'
some_dict = dict()

changed_list = somelist.replace('=sssss', '').replace('&&', '&').split('&')

for element in changed_list:
    el = element.split('=')
    some_dict[el[0]] = el[1]

print(some_dict)
