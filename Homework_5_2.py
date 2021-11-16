with open('new_fail_5_2.txt') as file:
    lines = file.readlines()
    str_count = 0
    for nums, nums_line in enumerate (lines):
        str_count +=1
        wrd_count = len (nums_line.split())
        print (f'{nums + 1} - {wrd_count} слов')
    print (f'{str_count} строк')