with open('test.txt','w') as new_file:
    str = input('Ведите текст : ')
    while str:
        new_file.write(f'{str}\n')
        str = input('Ведите текст: ')
