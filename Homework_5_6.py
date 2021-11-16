res = {}

with open('subjects.txt') as file:
    lines = file.readlines()
    for l in lines:
        mean = l.split()
        hour = 0
        for i in mean[1:]:
            if i != '-':
                x = '0'
                for n in i:
                    if n.isdigit():
                        x += n
                    else:
                        break
                hour += int (x)
        res.update({mean[0].strip(':'): hour})
print(res)