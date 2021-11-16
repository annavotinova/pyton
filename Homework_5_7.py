import json

company = {}
firm_count = 0
firm_sum = 0

with open('info_company.txt') as file:
    lines = file.readlines()
    for l in lines:
        mean = l.split()
        prof = int(mean[2]) - int(mean[3])
        company.update({mean[0]: prof})
        firm_count += 1
        firm_sum += prof

aver = firm_sum / firm_count
res = [company, {'средняя выручка' : aver}]

with open("finish.json", 'w') as new_file:
    json.dump(res, new_file)