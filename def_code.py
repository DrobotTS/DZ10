import random, json
import os
# перезапуск програмы
def restart_param():
    with open('sys.json', 'w') as sys_file:
        defolt = json.dump({"price": open_file_config()['price'], "valet": open_file_config()['valet'],
                            "usd_valet": open_file_config()['usd_valet']}, sys_file)
        return defolt
def open_file_config():
    with open('config.json', 'r') as config_file:
        data = json.load(config_file)
    return data
# запись в файл sys
def write_file_sys():
    if os.stat("sys.json").st_size == 0:
        return
    else:
        with open('sys.json', 'w') as sys_file:
            json.dump({"price": price, "valet": valet, "usd_valet": usd_valet}, sys_file)
    return write_file_sys
# чтение файла sys
def read_file_sys():
    with open('sys.json', 'r') as sys_file:
        write_file = json.load(sys_file)
    return write_file
# Смена курса
def next_param():
    global price, valet, usd_valet
    valet = read_file_sys()['valet']
    usd_valet = read_file_sys()['usd_valet']
    price = round(random.uniform(open_file_config()['price'] - open_file_config()['delta'],
                                open_file_config()['price'] + open_file_config()['delta']), 1)
    return price
# Вывод курса
def rate_param():
    if os.stat("sys.json").st_size == 0 or read_file_sys()["price"] == 0:
        return "Введите RESTART"
    else:
        rate = read_file_sys()['price']
    return rate

# Функция покупки определенного колличества долларов
def buy_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Введите RESTART")
    elif read_file_sys()['valet'] <= 0:
        price = read_file_sys()['price']
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        print("У вас нет грн для покупки")
    elif read_file_sys()['valet'] > 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        usd = float(input("Введите сколько хотите купить долларов: "))
        usd_buy = usd * read_file_sys()['price']
        if read_file_sys()['valet'] - int(usd_buy) < 0:
            print("У вас недостаточно грн", "\nВаш счет:", read_file_sys()['valet'], "ГРН\n"
                                                 "Курс:", read_file_sys()['price'],"Долл/грн")
        else:
            valet = read_file_sys()['valet'] - usd_buy
            usd_valet = read_file_sys()['usd_valet'] + float(usd)
            price = read_file_sys()['price']
def buy_uah_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Введите RESTART")
    elif read_file_sys()['usd_valet'] <= 0:
        price = read_file_sys()['price']
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        print("У вас нет Долларов для продажи")
    elif read_file_sys()['usd_valet'] > 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        usd = float(input("Введите сколько хотите купить грн: "))
        usd_buy = usd / read_file_sys()['price']
        if read_file_sys()['usd_valet'] - int(usd_buy) < 0:
            print("У вас недостаточно долларов", "\nВаш счет:", read_file_sys()['usd_valet'], "ГРН\n"
                                                 "Курс:", read_file_sys()['price'],"Долл/грн")
        else:
            usd_valet= read_file_sys()['usd_valet'] - round(usd_buy,2)
            valet = read_file_sys()['valet'] + float(usd)
            price = read_file_sys()['price']
# купить на все грн доллары
def buy_all_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Введите RESTART")
    elif read_file_sys()['valet'] <= 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        print("У вас нет грн для покупки")
    else:
        price = read_file_sys()['price']
        usd = read_file_sys()['valet']/read_file_sys()['price'] # покупка доллара на все
        valet = read_file_sys()['valet'] - read_file_sys()['valet'] # перезапись грн кошелька
        usd_valet = round(read_file_sys()['usd_valet'] + usd, 2) # перезапись долл. кошелька
        print("USD:", usd_valet, "ГРН:", valet)
# вывести содержание кошелька
def available_param():
    if os.stat("sys.json").st_size == 0:
        print("Введите RESTART")
    else:
        print("USD:", read_file_sys()['usd_valet'], "ГРН:", read_file_sys()['valet'])
# Продать все доллары
def sell_all_param():
    global valet, usd_valet, price
    if os.stat("sys.json").st_size == 0:
        print("Введите RESTART")
    elif read_file_sys()['usd_valet'] <= 0:
        valet = read_file_sys()['valet']
        usd_valet = read_file_sys()['usd_valet']
        price = read_file_sys()['price']
        print("У вас нет долларов для продажи")
    else:
        price = read_file_sys()['price']
        buy_uah = read_file_sys()['usd_valet']*read_file_sys()['price']
        usd_valet = read_file_sys()['usd_valet'] - read_file_sys()['usd_valet']
        valet = round(read_file_sys()['valet'] + buy_uah, 2)
        print("USD:", usd_valet, "ГРН:", valet)
def info_param():
    print("RESTART - Перезапуск програмы;\nNEXT - обновить курс;\nRATE - Вывести курс;\nBUY - купить доллары;\n"
              "BUY_ALL - купить на все доллары;\nSELL_ALL - продать все доллары;\nAVAILABLE - вывод баланса;\n"
             "BUY_UAH - купить гривну;\nINFO - Вывод команд.")
