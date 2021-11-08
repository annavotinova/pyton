def int_func(text):
    word = text[0].upper() + text[1:]
    return word

str = input ('Введите строк, в которой слова будут разделены пробелом: ')
for word in str.split(' '):
    print (f'{int_func(word)}', end=' ')