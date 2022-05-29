import csv


attributes = 'scripts/file_types.csv'

with open(attributes, 'r') as csvfile:
    attrs = csv.DictReader(csvfile)

    with open('.gitattributes', 'w') as file:
        file.write('* -text\n')
        for attr in attrs:
            ftype = attr['file type']
            attribute = attr['attributes']

            if attribute == 'binary':
                file.write(f'{ftype} filter=lfs diff=lfs merge=lfs -text\n')
