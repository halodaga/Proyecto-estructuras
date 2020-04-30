import os
from os import system
from structures import *
from pickles import *
from time import time 
from datetime import date
import sys
sys.path.insert(1, '../lib/prettytable-0.7.2')
from  prettytable import PrettyTable

def option():
    while True:
        menuElements = ["Menú principal","- m ----- Mostrar todo", "- l ----- Añadir", "- c ----- Editar elemento",
         "- b ----- Buscar","- o ----- Ordenar alfabeticamente", "- d ----- Eliminar todo", "- e ----- Eliminar" ,"- g ----- Guardar", "- q ----- Salir"]
        #Print menu with format
        print(menuElements[0].center(os.get_terminal_size().columns,'-'),  end = '')

        for x in range(1, len(menuElements)):
            print(menuElements[x].ljust(33).center(os.get_terminal_size().columns),  end = '')
            
        print(''.center(os.get_terminal_size().columns,'-'))

        answer = input()

        if answer == "m":
            show()
        elif answer == "l":
            load()
        elif answer == "c":
            searchToEdit()
        elif answer == "b":
            search()
        elif answer == "d":
            deleteEverything() 
        elif answer == "e":
            delete()

        elif answer == "o":
            showSort()
        elif len(answer) > 0 and answer.split()[0] == "DEV":
            if len(answer.split()) > 1:
                if answer.split()[1] == "--help":
                    print("-l agregar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("-d eliminar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("-s buscar masivamente".ljust(23).center(os.get_terminal_size().columns),  end = '')
                    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
                    _ = input()
                    if os.name == "posix":
                        os.system("clear")
                    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                        os.system("cls")
                elif answer.split()[1] == "-l":
                    massiveLoad()
                elif answer.split()[1] == "-d":
                    massiveDelete()
                elif answer.split()[1] == "-s":
                    masiveSearch()
                else:
                    print("Valor incorrecto, --help para ver opciones".center(os.get_terminal_size().columns,' '))
            else:
                print("Parametro esperado".center(os.get_terminal_size().columns,' '))  
                print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
                _ = input()
                if os.name == "posix":
                    os.system("clear")
                elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                    os.system("cls")
        elif answer == "q":
            if os.name == "posix":
                os.system("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            print("Hasta pronto".center(os.get_terminal_size().columns,'*'))
            return False

        else:
            if os.name == "posix":
                os.system("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            print("La opcion es incorrecta, ingresela de nuevo")

def notDefined():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    print("Lo sentimos, esta utilidad estará disponible en futuras versiones.".center(os.get_terminal_size().columns))
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def show():
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for index in range(0,almacen.size):
        if almacen.data[index] != 0:
            t.add_row(almacen.data[index])
    print(t)

    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def load():
    try:
        amnt = int(input("Ingrese el numero de elementos a cargar: "))
        almacen=cargarSesion("Default")
        t0=time()
        for i in range(amnt):
            lista=[]

            lista.append(input("Ingrese nombre: "))
            lista.append(float(input("Ingrese precio: ")))
            lista.append(int(input("Ingrese codigo de barras: ")))
            lista.append(int(input("Ingrese cantidad: ")))

            lista.append(date.today())
            #x = randomword(6)
            #lista = [x,23,i,1,"12-02-12"] #usar para pruebas random
            almacen.add(lista)
        guardarSesion("Default",almacen)
        print("Elementos añadidos")
    except:
        print("comando invalido, presione enter para regresar al menú")

    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def delete():
    amnt = int(input("Ingrese el numero de elementos a eliminar: "))

    almacen=cargarSesion("Default")

    for _ in range(amnt):
        toDelete = input("Ingrese nombre de objeto a eliminar: ")
        amntToDelete = int(input("Ingrese la cantidad a eliminar: "))
        almacen.delet(toDelete, amntToDelete)
    guardarSesion("Default",almacen)
    print("Elemento eliminado")
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def search():
    amnt = int(input("Ingrese el numero de elementos a buscar: "))
    almacen=cargarSesion("Default")
    searched = 0
    while searched < amnt:
        toSearch = input("Ingrese el elemento a buscar: ")
        elmt = almacen.search(toSearch)
        searched +=1
        if elmt != None:
            printElement(elmt,almacen)

    guardarSesion("Default", almacen)
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    _ = system('cls') 
def searchToEdit():
    amnt = int(input("Ingrese el numero de elementos a editar: "))
    almacen=cargarSesion("Default")
    edited = 0
    while edited < amnt:
        toSearch = input("Ingrese el nombre del elemento a editar: ")
        elmt = almacen.search(toSearch)
        edited +=1
        if elmt != None:
            printElement(elmt,almacen)
            edit(elmt, almacen)
        print()

    guardarSesion("Default", almacen)
    print("Elemento editado".center(os.get_terminal_size().columns))
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
def edit(elmt, almacen):
    lista=[]
    lista.append(input("Ingrese el nuevo nombre: "))
    lista.append(float(input("Ingrese el nuevo precio: ")))
    lista.append(int(input("Ingrese el nuevo codigo de barras: ")))
    lista.append(int(input("Ingrese la nueva cantidad: ")))
    lista.append(date.today())
    almacen.edit(elmt, lista)

def massiveLoad():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    try:
        amnt = int(input("Ingrese el numero de elementos a cargar: "))
        almacen=cargarSesion("Default")
        t0 = time()
        for i in range(amnt):
            x = randomword(6)
            lista = [x,23,i,1,"12-02-12"]
            almacen.add(lista)
        guardarSesion("Default", almacen)
        tf = time()
        print("El tiempo para añadir ", amnt, " elementos fue de: ", tf - t0,"s" )
        print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    except:
        print("comando invalido, presione enter para regresar al menú")
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def massiveDelete():
    almacen = cargarSesion("Default")
    print("eliminando todos los elementos un por uno")
    t0 = time()
    n = almacen.size
    for i in range(n):
        almacen.data[i] = 0
    alamacen.size = 0
    guardarSesion("Default", almacen)
    tf = time()
    print("El tiempo para eliminar todos elementos fue de: ", tf - t0,"s" )
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def masiveSearch():
    almacen = cargarSesion("Default")
    print("Pueden buscar un maximo de:", almacen.size, "elementos.")
    try:
        amnt = int(input("Buscar: "))
        t0 = time()
        lista = list(almacen.dictNames.keys())
        temp = 0
        if amnt <= almacen.size:
            while temp < amnt:
                almacen.search(lista[temp])
                temp += 1

            tf = time()
            print("El tiempo para buscar ", amnt, " elementos fue de: ", tf - t0,"s" )
            print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
        else:
            print("No se puede buscar esta cantidad de elementos")
        _ = input()
    except:
        print("comando invalido, presione enter para regresar al menú")
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def loadDataAuto():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for x in almacen.dictNames:
        if almacen.data[int(almacen.dictNames.get(x))] != 0:
            t.add_row(almacen.data[int(almacen.dictNames.get(x))])
    print(t)
    print("Presione enter para regresar el menu".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def deleteEverything():
    os.remove("../data/Default.pickle")
    crearSesion("Default")

    print("Datos eliminados".center(os.get_terminal_size().columns))
    _ = input()
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def printElement(index, almacen):
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    if almacen.data[index] != 0:
        t.add_row(almacen.data[index])
    print(t)

def showSort():
    almacen = cargarSesion("Default")
    t = PrettyTable(['Nombre', 'Precio', 'Codigo de barras', 'Cantidad', 'Fecha de agregado'])
    for x in almacen.bSort():
        t.add_row(almacen.data[int(almacen.dictNames.get(x))])
    print(t)


if __name__ == '__main__':
    if not os.path.exists("../data/Default.pickle"):
        crearSesion("Default")
    
    option()

			
