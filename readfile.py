with open ('file.txt', 'w', encoding='utf-8') as file:
    file.write('Hello' + '\n')
    file.write('' + '\n')
    file.write('world')
    file.truncate(0)