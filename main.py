import sys
import def_code
import os

name_code, param_console = sys.argv

def main():
    if param_console == "RESTART":
        def_code.restart_param()
        print("Игра перезапущена, введите INFO для вывода команд")
    elif param_console == "NEXT":
        if os.stat("sys.json").st_size == 0:
            print("Введите RESTART")
        else:
            print("Курс обновлен:", def_code.next_param())
            def_code.write_file_sys()
    elif param_console == "RATE":
        print(def_code.rate_param())
    elif param_console == "BUY":
        def_code.buy_param()
        def_code.write_file_sys()
    elif param_console == "BUY_UAH":
        def_code.buy_uah_param()
        def_code.write_file_sys()
    elif param_console == "BUY_ALL":
        def_code.buy_all_param()
        def_code.write_file_sys()
    elif param_console == "AVAILABLE":
        def_code.available_param()
    elif param_console == "SELL_ALL":
        def_code.sell_all_param()
        def_code.write_file_sys()
    elif param_console == "INFO":
        def_code.info_param()
    else: print("Нет такой команды, введите INFO")

sys.exit(main()) if __name__ == '__main__' else print("error")


