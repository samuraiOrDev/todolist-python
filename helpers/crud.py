import csv
import datetime
import os 

from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import clear
from tabulate import tabulate

'''
Genera el un archivo y unos datos de semilla si no 
existe nada.
'''
def generate_task_lists():
    if os.path.exists('tasks.csv'):
        return
    tasks = [
        ["1","Test", "Description Test", "Pendiente", "2022-01-01", "--"],
    ]

    over_file(tasks)

'''
Muestra la lista de tareas en formato tabla
'''
def list_tasks():
    clear()
    print(Style.RESET_ALL)
    with open('tasks.csv', 'r') as file:
       tasks = csv_to_list(file)
       colored_tasks = []
       if len(tasks) == 1 and isinstance(tasks[0], list):
            print(Fore.YELLOW + "#####################################")

            print(Fore.YELLOW + "No hay tareas actualmente registradas")

            print(Fore.YELLOW + "#####################################")
            return
       for task in tasks: 
           colored_task = []
           for field in task:
                if field == "Pendiente": 
                   colored_task.append(Fore.RED + field + Style.RESET_ALL)
                elif field == "En Curso": 
                    colored_task.append(Fore.YELLOW + field + Style.RESET_ALL)
                elif field == "Completada": 
                    colored_task.append(Fore.GREEN + field + Style.RESET_ALL)
                else:
                    colored_task.append(field +  Style.RESET_ALL)
           colored_tasks.append(colored_task)
           
       print( tabulate(colored_tasks, headers="firstrow", tablefmt="fancy_grid"))

'''
Agrega un TAREA
'''
def add_task():
    try:
        print("Ingrese las caracteísticas de su tarea: ")
        with open('tasks.csv', 'r') as file:
            tasks = csv_to_list(file)
            if len(tasks) == 1 and isinstance(tasks[0], list):
                last_id = 0
            else:
                last_id = int(tasks[-1][0]) if tasks else 0
        new_id = last_id + 1
        
        
        # Obtener los valores para los campos restantes de la tarea
        titulo = input("Ingrese el título: ")
        descripcion = input("Ingrese la descripción: ")
        estado = input("Ingrese el estado: ")
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        
         # Validar que el título y la descripción no estén vacíos
        if not titulo or not descripcion:
            raise ValueError(Fore.RED + "El título y la descripción no pueden estar vacíos.")
        
        # Validar que el estado sea uno de los valores permitidos
        estados_permitidos = ['Completada', 'En Curso', 'Pendiente']
        if estado not in estados_permitidos:
            raise ValueError(Fore.RED + "El estado debe ser 'Completada', 'En Curso' o 'Pendiente'.")
        
        # Validar que las fechas tengan el formato correcto
        try:
            datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
            datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
        except ValueError:
            raise ValueError(Fore.RED + "Las fechas deben tener el formato YYYY-MM-DD.")
        
        with open('tasks.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(new_id), titulo, descripcion, estado, fecha_inicio, fecha_fin])
        
        print(Fore.GREEN + "Tarea agregada exitosamente.")
    except Exception as e:
        print("Error al agregar la tarea:", str(e))

'''
Eliminar tarea por id
'''
def delete_task(): 
    try:
        task_id = input("Ingrese el identificador de la tarea a eliminar: ")
        with open('tasks.csv', 'r') as file:
            tasks = csv_to_list(file)
        task_found = False
        for task in tasks:
            if task[0] == task_id:
                tasks.remove(task)
                task_found = True
                break
        if not task_found:
            print(Fore.RED + "No se encontró una tarea con el identificador proporcionado o no es un identificador válido.")
            return
        over_file(tasks)
        print(Fore.GREEN + f"Tarea {task_id} eliminado con éxito")
    except Exception as e:
      print("Error al eliminar la tarea:", str(e))

'''
Buscar tarea por id
'''
def search_task(): 
    try:
        clear()
        task_id = input("Ingrese el identificador de la tarea a buscar: ")
        with open('tasks.csv', 'r') as file:
            tasks = csv_to_list(file)
        task_found = False
        colored_tasks = []
        for task in tasks:
            colored_task = []
            if task[0] == 'ID':
                for field in task:
                    colored_task.append(Fore.CYAN + field )
                colored_tasks.append(colored_task)
            if task[0] == task_id:
                for field in task:
                    if field == "Pendiente": 
                        colored_task.append(Fore.RED + field)
                    elif field == "En Curso": 
                            colored_task.append(Fore.YELLOW + field )
                    elif field == "Completada": 
                            colored_task.append(Fore.GREEN + field )
                    else:
                            colored_task.append(Fore.CYAN + field )
                colored_tasks.append(colored_task)
                task_found = True
                break
        print( tabulate(colored_tasks, headers="firstrow", tablefmt="fancy_grid"))
        if not task_found:
            print(Fore.RED + "No se encontró una tarea con el identificador proporcionado o no es un identificador válido.")
            return
        over_file(tasks)
    except Exception as e:
      print("Error al eliminar la tarea:", str(e))


'''
Actualizar tarea
'''
def update_task():
    try:
        clear()
        task_id = input("Ingrese el identificador de la tarea a buscar: ")
        with open('tasks.csv', 'r') as file:
            tasks = csv_to_list(file)
        # Obtener los valores nuevos de la tarea para los campos restantes de la tarea
        titulo = input("Ingrese el título: ")
        descripcion = input("Ingrese la descripción: ")
        estado = input("Ingrese el estado: ")
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        
         # Validar que el título y la descripción no estén vacíos
        if not titulo or not descripcion:
            raise ValueError(Fore.RED + "El título y la descripción no pueden estar vacíos.")
        
        # Validar que el estado sea uno de los valores permitidos
        estados_permitidos = ['Completada', 'En Curso', 'Pendiente']
        if estado not in estados_permitidos:
            raise ValueError(Fore.RED + "El estado debe ser 'Completada', 'En Curso' o 'Pendiente'.")
        
        # Validar que las fechas tengan el formato correcto
        try:
            datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
            datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
        except ValueError:
            raise ValueError(Fore.RED + "Las fechas deben tener el formato YYYY-MM-DD.")
        
        task_found = False
        for task in tasks:
            if task[0] == task_id:
                task[1] = titulo
                task[2] = descripcion
                task[3] = estado
                task[4] = fecha_inicio
                task[5] = fecha_fin
                task_found = True
                break
        if not task_found:
            print(Fore.RED + "No se encontró una tarea con el identificador proporcionado o no es un identificador válido.")
            return
        over_file(tasks)
        print(Fore.GREEN + f"Tarea {task_id} actualizada con éxito")
    except Exception as e:
        print("Error al agregar la tarea:", str(e))


'''
Eliminación del Archivo
'''
def delete_all_tasks():
    if not os.path.exists('tasks.csv'):
        print("No existe ningún archivo de tareas.")
        return
    tasks = []
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID","Titulo", "Descripción", "Estado", "Fecha Inicio", "Fecha Fin"])
        writer.writerows(tasks)
    
    print("Todas las tareas han sido eliminadas exitosamente.")

'''
CsvToList
'''
def csv_to_list (file) -> list:
    reader = csv.reader(file)
    return list(reader)


'''
Over_File
'''

def over_file(tasks) -> None:
    file_exists = os.path.exists('tasks.csv')
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID","Titulo", "Descripción", "Estado", "Fecha Inicio", "Fecha Fin"])
        writer.writerows(tasks)