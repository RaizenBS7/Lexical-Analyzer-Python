
def main():
    cadena_resultado = ''
    columna = 0
    alfanumeric_list = []
    ascii_list = []
    edo = 0
    constantes = []
    tokens = []
    variables = []
    variables.clear()

    reservadas = {"main": "501",
                "start": "502",
                "end": "503",
                "int": "504",
                "dec": "505",
                "string": "506",
                "condition": "507",
                "during": "508",
                "do": "509",
                "repeat": "510",
                "then": "511",
                "and": "5012",
                "or": "513",
                "not": "514"
                } #Se crea el diccionario de palabras reservadas
    simbolos = {  "<": "1001",
                  ">": "1002",
                  "+": "1003",
                  "-": "1004",
                  "=": "1005",
                  "/": "1006",
                  "*": "1007",
                  ".": "1008",
                  ",": "1009",
                  ";": "1010",
                  ":": "1011",
                  "(": "1012",
                  ")": "1013",
                  "'": "1014",
                  "<>": "1015",
                  "<=": "1016",
                  ">=": "1017",
                  "esp": "1018"
                  } #se crea el diccionario de cimbolos especiales reservados

    archivo = open('Lector.txt', 'r') #Se indica el archivo que leera
    # inicia bucle infinito para leer línea a línea
    while True:
        linea = archivo.readline()  # lee línea
        #print(linea)

        for char in linea:  # Leyendo caracter por caratcer
            alfanumeric_list.append(char)  # agregamos los caracteres a las listas
            ascii_list.append(ord(char))
            #print(ascii_list)
        #agregamos un caracter al final de cada linea para que lea el ultimo caracter de la linea
        if (len(linea)-1):
            alfanumeric_list.append(" ")
            ascii_list.append(3)  # el 3 en ascii es fin de linea

        #Recorrer el array creado para ir detectando: columna, estado, salida final.
        i = 0
        while i < len(ascii_list):
            #Se obtiene el numero de columna y el nuevo estado
            if edo >= 0:
                #print(edo)
                columna = obtener_columna(ascii_list[i])
                edo = matriz[edo][columna] #Nos movemos entre la matris de estados

                #Agregando el caracter alfanumerico a la cadena del resultado final.
                if (edo <= 34 or (edo >= 300 and edo <= 313)):
                    cadena_resultado += alfanumeric_list[i]
            i += 1
            #Si el nuevo estado es mayor que 34, quiere decir que ya hay una salida o un error
            if edo > 17: #Regresamos un lugar al puntero dentro de la lista para que vuelva a leer el ultimo caracter
                i -= retornar_lugar(edo)
                # se quitan todos los espacios que se agregaron a la cadena.
                cadena_resultado = cadena_resultado.replace(" ", "")
                cadena_resultado = cadena_resultado.replace("\n", "")
                #Obtenemos la salida o el error que se ha detectado
                obtener_resultado(edo, cadena_resultado)
                if edo == 204:
                    if cadena_resultado in reservadas:
                        tk = reservadas[cadena_resultado]
                        tokens.append([500, tk])
                    else:
                        if cadena_resultado not in variables:
                            variables.append(cadena_resultado)
                            ind = variables.index(cadena_resultado)
                            tokens.append([2000, ind])
                        else:
                            ind = variables.index(cadena_resultado)
                            tokens.append([2000, ind])
                if (edo >= 205 and edo <= 208 or (edo >=300 and edo <= 311)):
                    if cadena_resultado in simbolos:
                        tk = simbolos[cadena_resultado]
                        tokens.append([1000, tk])
                if(edo >= 200 and edo <= 203):
                    if cadena_resultado not in constantes:
                        constantes.append(cadena_resultado)
                        tk = constantes.index(cadena_resultado)
                        tokens.append([700, tk])

                cadena_resultado = ""
                edo = 0

        if not linea:
            break  # Si no hay más se rompe bucle
    #    print(alfanumeric_list)  # Muestra la línea leída
    #    print(ascii_list)
        alfanumeric_list.clear()
        ascii_list.clear()

    archivo.close()  # Cierra archivo


    print(tokens)#-------------------
    #matriz de estados
matriz=[#   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17
        # dig, E/e, let,   <,   >,   +,   -,   =,   /,   *,   .,   ,,   ;,   :,   (,   ),   ", esp,
        [   1,  10,  10,  11,  12, 305, 306, 309,  14, 308, 310, 307, 308,  13, 303, 304, 17,   0],# 0
        [   1,   2, 200, 200, 200, 200, 200, 200, 200, 200,   5, 200, 200, 200, 200, 200, 200, 200],# 1
        [ 500, 500, 500, 500, 500,   3,   3, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 2
        [   4, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 3
        [   4, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201],# 4
        [   6, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 5
        [   6,   7, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202],# 6
        [ 500, 500, 500, 500, 500,   8,   8, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 7
        [   9, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 8
        [   9, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203],# 9
        [  10,  10,  10, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204],# 10
        [ 205, 205, 205, 205, 301, 205, 205, 300, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205],# 11
        [ 206, 206, 206, 302, 206, 206, 206, 302, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206],# 12
        [ 207, 207, 207, 207, 207, 303, 207, 311, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207],# 13
        [ 208, 208, 208, 208, 208, 208, 208, 208, 208,  15, 208, 208, 208, 208, 208, 208, 208, 208],# 14
        [  15,  15,  15,  15,  15,  15,  15,  15,  15,  16,  15,  15,  15,  15,  15,  15,  15,  15],# 15
        [  15,  15,  15,  15,  15,  15,  15,  15, 312,  15,  15,  15,  15,  15,  15,  15,  15,  15],# 16
        [  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17, 313,  17] # 17
        ]


def obtener_columna(charAscii):
    if (charAscii >= 48 and charAscii <= 57):
        columna = 0

      #detectar E e
    elif (charAscii == 69 or charAscii == 101):
        columna = 1

      #detectar LETRAS
    elif (charAscii >= 65 and charAscii <= 90 or charAscii >= 97 and charAscii <= 122):
        columna = 2

      #detectar < mayor que
    elif (charAscii == 60):
        columna = 3

      #detectar > menor que
    elif (charAscii == 62):
        columna = 4

      #detectar +
    elif (charAscii == 43):
        columna = 5

      #detectar -
    elif (charAscii == 45):
        columna = 6

      #detectar =
    elif (charAscii == 61):
        columna = 7

      #detectar /
    elif (charAscii == 47):
        columna = 8

      #detectar *
    elif (charAscii == 42):
        columna = 9

      #detectar .
    elif (charAscii == 46):
        columna = 10

      #detectar ,
    elif (charAscii == 44):
        columna = 11

      #detectar ;
    elif (charAscii == 59):
        columna = 12

      #detectar : doble punto
    elif (charAscii == 58):
        columna = 13

      #detectar ( parentesis abierto
    elif (charAscii == 40):
        columna = 14

      #detectar ) parentesis cerrado
    elif (charAscii == 41):
        columna = 15

      #detectar " comilla double
    elif (charAscii == 34):
        columna = 16

      #detectar espacio #detectar nueva linea #detectar retorno de carro #detectar fin de texto
      #detectar si es NULL
    elif (charAscii == 32 or charAscii == 10 or charAscii == 13 or charAscii == 3 or charAscii == 0):
          columna = 17

    else:
        print("error caracter no reconocido" + str(charAscii))

    return columna #Nos movemos entre las columnas de la matriz


def obtener_resultado(edo, cadena_resultado): #Imprimimos la cadena resultado que se a obtenido con su respectivo estado y Tipo
    if edo == 0:
        print(cadena_resultado + "Estado: " + str(edo) + "Espacio")

    elif edo == 200:
        print(cadena_resultado + " Estado " + str(edo) + ": NúmeroEntero ")

    elif edo == 201:
        print(cadena_resultado + " Estado " + str(edo) + ": Número Entero Con Exponente ")

    elif edo == 202:
        print(cadena_resultado + " Estado " + str(edo) + ": Número Decimal ")

    elif edo == 203:
        print(cadena_resultado + " Estado " + str(edo) + ": Número Decimal Con Exponente ")  # *******

    elif edo == 204:
        print(cadena_resultado + " Estado " + str(edo) +  ": Identificador ")  # regresar un espacio

    elif edo == 205:
        print(cadena_resultado + " Estado " + str(edo) + ": < ")

    elif edo == 206:
        print(cadena_resultado + " Estado " + str(edo) + ": > ")

    elif edo == 207:
        print(cadena_resultado + " Estado " + str(edo) + ": : ")

    elif edo == 208:
        print(cadena_resultado + " Estado " + str(edo) + ": / ")  # regresar un espacio

    elif edo == 300:
        print(cadena_resultado + " Estado " + str(edo) + ": <= ")

    elif edo == 301:
        print(cadena_resultado + " Estado " + str(edo) + ": <> ")

    elif edo == 302:
        print(cadena_resultado + " Estado " + str(edo) + ": >= ")

    elif edo == 303:
        print(cadena_resultado + " Estado " + str(edo) + ": ( ")

    elif edo == 304:
        print(cadena_resultado + " Estado " + str(edo) + ": ) ")

    elif edo == 305:
        print(cadena_resultado + " Estado " + str(edo) + ": + ")

    elif edo == 306:
        print(cadena_resultado + " Estado " + str(edo) + ": - ")

    elif edo == 307:
        print(cadena_resultado + " Estado " + str(edo) + ": , ")  # regresar un espacio

    elif edo == 308:
        print(cadena_resultado + " Estado " + str(edo) + ": ; ")  # regresar un espacio

    elif edo == 309:
        print(cadena_resultado + " Estado " + str(edo) + ": = ")

    elif edo == 310:
        print(cadena_resultado + " Estado " + str(edo) + ": . ")

    elif edo == 311:
        print(cadena_resultado + " Estado " + str(edo) + ": := ")  # regresar un espacio

    elif edo == 312:
        print(cadena_resultado + " Estado " + str(edo) + ": Comentario encontrado")

    elif edo == 313:
        print(cadena_resultado + " Estado " + str(edo) + ": Texto encontrado ")

    elif edo == 500:
        print(cadena_resultado + " Error " + str(edo) + ": Se esperaba otro signo")

    elif edo == 504:
        print(cadena_resultado + " Error " + str(edo) + ": Caracter no reconocido.")

    else:
        print('caracter no Identificado ' + str(edo))


def retornar_lugar(edo):
    back = 0 #si los estados fiales no son con asterisco, no regresamos un espacio para no perder el caracter

    if (edo >= 200 and edo <= 208):#si los estados finales son con asterisco, regresamos un espacio
        back = 1

    return back


if __name__ == '__main__':
  main()
#Programa realizado por Maximiliano Garcia De Santiago
#Copyright (c) all rights reserved
#Contato [Facebook]:Max Garcia [Email]:max-gds96@hotmail.com
