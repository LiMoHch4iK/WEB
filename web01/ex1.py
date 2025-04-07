from zipfile import ZipFile

with ZipFile('archive.zip', 'a') as myzip:
    myzip.write('test.txt')
    print(myzip.namelist())