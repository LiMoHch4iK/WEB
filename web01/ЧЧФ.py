def human_read_format(size):
    if size < 2 ** 10:
        return f'{size}Б'
    if size < 2 ** 20:
        return f'{round(size / 2 ** 10)}КБ'
    if size < 2 ** 30:
        return f'{round(size / 2 ** 20)}МБ'
    return f'{round(size / 2 ** 30)}ГБ'


print(human_read_format(1023))
print(human_read_format(15000))
