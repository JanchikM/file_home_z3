import os

total = {}
for i in os.listdir():
    if i.endswith('.txt') and i != 'new.txt':
        with open(i, encoding='utf-8') as f:
            line = f.readlines()
            len_line = len(line)
            info = (f'{i}\n'
                    f'{len_line}\n'
                    f'{"".join(line)}\n')
            total[len_line] = info
            all = sorted(total.items())
for x in all:
    with open('new.txt', 'a', encoding='utf-8') as f:
        f.writelines(x[1])