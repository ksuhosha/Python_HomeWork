from datetime import datetime


def Logger(a, b, x, sim):
    calc_dict = {1: '*', 2: '/', 3: '+', 4: '-'}
    time = datetime.now().strftime('%m.%d.%y %H:%M')
    with open('calc/log.csv', 'a') as file:
        file.write(f"{time}\t{a} {calc_dict[sim]} {b} = {x} \n")
