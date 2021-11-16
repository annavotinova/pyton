with open ('Pay.txt') as file:
    lines = file.readlines()
    people = {}
    sum_pay = 0
    for i in lines:
        ppl_pay = i.split()
        people.update({ppl_pay[0]: int(ppl_pay[1])})
        sum_pay += int(ppl_pay[1])
aver_pay = sum_pay / len(people)
print(f'Средняя зарплата = {aver_pay}')

for sur_name, money in people.items():
    if money < 20000:
        print(f'{sur_name} - {money}')
