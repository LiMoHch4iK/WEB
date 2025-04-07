from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    for el in myzip.namelist():
        if el[-1] == '/':
            count = el[:-1].count('/')
            print('  ' * count, el.split('/')[-2], sep='')
        else:
            count = el.count('/')
            print('  ' * count, el.split('/')[-1], sep='')

