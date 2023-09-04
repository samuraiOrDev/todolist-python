import csv
import os 

from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import clear
from tabulate import tabulate

from helpers.crud import  add_task, list_tasks, delete_task, search_task, update_task, delete_all_tasks,  generate_task_lists


def main():
    generate_task_lists()
    while True:
        print(Fore.CYAN + "Seleccione una opción:")
        print("")
        print(Fore.CYAN + "1." + Fore.YELLOW  + " Listar tareas")
        print(Fore.CYAN + "2." + Fore.YELLOW  + " Agregar tarea")
        print(Fore.CYAN + "3." + Fore.YELLOW  + " Eliminar tarea")
        print(Fore.CYAN + "4." + Fore.YELLOW  + " Buscar tarea por Identificador")
        print(Fore.CYAN + "5." + Fore.YELLOW  + " Actualizar tarea por Identificador")
        print(Fore.CYAN + "6." + Fore.YELLOW  + " Eliminar todas las tareas")
        print(Fore.CYAN + "7." + Fore.YELLOW  + " Salir")
        print("")
        option = input("Opción: ")

        if option == '1':
            list_tasks()
        elif option == '2':
            add_task()
        elif option == '3':
            delete_task()
        elif option == '4':
            search_task()
        elif option == '5':
            update_task()
        elif option == '6':
            delete_all_tasks()
        elif option == '7':
            break
        else:
            print(Fore.RED + "Opción inválida. Intente nuevamente.")
    print("¡Hasta luego!")
    print(Style.RESET_ALL)
    print("\033[0m")

if __name__ == '__main__':
    main()