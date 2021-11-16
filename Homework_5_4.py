numbers = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}

with open('numbers.txt') as file, open('rus_file.txt', 'w') as rus_file:
    lines = file.readlines()
    for l in lines:
        mean = l.split()
        rus_nums = numbers.get(mean[0])
        rus_file.write(f'{l.replace(mean[0], rus_nums)}')