from pathlib import Path

file_types = []
for files in Path().rglob('**/*.*'):
    if files.suffix not in file_types:
        file_types.append(files.suffix)

with open('file_types.txt', 'w') as file:
    for i in file_types:
        if i == '':
            continue
        file.write('*{}, \n'.format(i))

