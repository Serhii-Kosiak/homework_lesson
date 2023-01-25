Eleks_company = ['name1', 'name2', 'name3']
Toshiba_company = ['name4', 'name5', 'name1']

# старый способ добавления, не использовать желательно, создает лишний лист:
Toshiba_Eleks = Toshiba_company + Eleks_company
print(Toshiba_Eleks)

# правильный способ, как был на лекции и ответ на дз где видно поглощение Тошибой:
Toshiba_company.extend(Eleks_company)
print(Toshiba_company)
