import os


def human_read_format(size):
    if size < 2 ** 10:
        return f'{size}Б'
    if size < 2 ** 20:
        return f'{round(size / 2 ** 10)}КБ'
    if size < 2 ** 30:
        return f'{round(size / 2 ** 20)}МБ'
    return f'{round(size / 2 ** 30)}ГБ'


def get_files_sizes():
    result = []
    for el in os.listdir():
        if os.path.isfile(el):
            result.append(f'{el} {human_read_format(os.path.getsize(el))}')
    return '\n'.join(result)


print(get_files_sizes())
