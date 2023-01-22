# You have a group of guests for the VIP box. The seats in the VIP box are all occupied by these guests.
# There is a group of guests in the common room and there are still places in it. Display 2 groups of guests in code.

# Вариант 1 - здесь есть список мест (к примеру взят от 101 до 107) в которых есть ключи и значения
# - VIP место или обычное General и их доступность к посадке. VIP мест к посадке доступных нет

Seats_person_group = {
    101: {'kind': 'VIP', 'available': False},
    102: {'kind': 'VIP', 'available': False},
    103: {'kind': 'VIP', 'available': False},
    104: {'kind': 'GENERAL', 'available': False},
    105: {'kind': 'GENERAL', 'available': False},
    106: {'kind': 'GENERAL', 'available': True},
    107: {'kind': 'GENERAL', 'available': True},

}

# Вариант решения №2, если имелось в виду просто неизменямость или изменяемость мест
Vip_seats = (1, 2, 3, 4, 5, 6, 7, 8, 9)
General_seats = ['111', '112', '113', '114', '115', '116', '117', '118', '119']
Vip_seats.append(10)
General_seats.append(120)
print(General_seats)
print(Vip_seats)
# мы не можем добавить к листу tuple 10 место, применить append. А к обычному листу - можем