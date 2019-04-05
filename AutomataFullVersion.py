def main():
  cadena_resultado =''
  columna = 0
  alfanumeric_list =[]
  ascii_list =[]
  edo = 0
  constantes = []
  tokens = []
  variables = []
  variables.clear()
  reservadas = {"for": "501",
                "case": "502",
                "catch": "503",
                "char": "504",
                "continue": "505",
                "length": "506",
                "private": "507",
                "try": "508",
                "this": "509",
                "break": "510",
                "false": "511",
                "true": "5012",
                "int": "513",
                "string": "514",
                "double": "515",
                "static": "516",
                "while": "517",
                "do": "518",
                "return": "519",
                "public": "520",
                "new": "521",
                "null": "522",
                "def": "523",
                "boolean": "524"
            }
  simbolos = {">":"1001",
              "<":"1002",
              "+":"1003",
              "-":"1004",
              "*":"1005",
              "/":"1006",
              "!":"1007",
              "%":"1008",
              "#":"1009",
              ".":"1010",
              ",":"1011",
              ";":"1012",
              ":":"1013",
              "{":"1014",
              "}":"1015",
              "[":"1016",
              "]":"1017",
              "(":"1018",
              ")":"1019",
              "|":"1020",
              "&":"1021",
              "'":"1022",
              '"':"1023",
              "esp":"1024"
            }

  archivo = open('Lector.txt','r')
  # inicia bucle infinito para leer línea a línea
  while True:
    linea = archivo.readline()  # lee línea
    #print(linea)

    for char in linea: #Leyendo caracter por caratcer

      alfanumeric_list.append(char) # agregamos los caracteres a las listas
      ascii_list.append(ord(char) )
      #print(ascii_list)
    #agregamos un caracter al final de cada linea para que lea el ultimo caracter de la linea
    if (len(linea)-1):
      alfanumeric_list.append(" ")
      ascii_list.append(3) # el 3 en ascii es fin de linea

    #Recorrer el array creado para ir detectando: columna, estado, salida final.
    i = 0
    while i < len(ascii_list):
      #Se obtiene el numero de columna y el nuevo estado
      if edo >= 0:
        #print(edo)
        columna = obtener_columna(ascii_list[i])
        edo = matriz[edo][columna]

        #Agregando el caracter alfanumerico a la cadena del resultado final.
        if (edo <= 34 or (edo >= 300 and edo <= 309)):
         # while True:
        #    if 97 in alfanumeric_list:
        #      alfanumeric_list.remove(97)
        #    break
          cadena_resultado+= alfanumeric_list[i]

      i+= 1

      #Si el nuevo estado es mayor que 34, quiere decir que ya hay una salida o un error
      if edo > 34:

        #Regresamos un lugar al puntero dentro de la lista para que vuelva a leer el ultimo caracter
        i-= retornar_lugar(edo)
        # se quitan todos los espacios que se agregaron a la cadena.
        cadena_resultado = cadena_resultado.replace(" ", "")
        cadena_resultado = cadena_resultado.replace("\n", "")
        #Obtenemos la salida o el error que se ha detectado
        obtener_resultado(edo, cadena_resultado)
        if edo == 204:
          if cadena_resultado in reservadas:
            tk = reservadas[cadena_resultado]
            tokens.append([500,tk])
            #print(tokens)
          else:
            if cadena_resultado not in variables:
              variables.append(cadena_resultado)
              ind = variables.index(cadena_resultado)
              tokens.append([2000,ind])
             # print("Mi tabla de variables--------------")
             # print(variables)
              #print("Mi tabla de tokens--------------")
              #print(tokens)
            else:
              ind = variables.index(cadena_resultado)
              tokens.append([2000,ind])
              #print("Mi tabla de variables--------------")
              #print(variables)
              #print("Mi tabla de tokens--------------")
              #print(tokens)
        if (edo >= 205 and edo <= 226):
            if cadena_resultado in simbolos:
                tk = simbolos[cadena_resultado]
                tokens.append([1000,tk])


        cadena_resultado = ""
        edo = 0


    if not linea:
      break  # Si no hay más se rompe bucle
#    print(alfanumeric_list)  # Muestra la línea leída
#    print(ascii_list)
    alfanumeric_list.clear()
    ascii_list.clear()

  archivo.close()  # Cierra archivo
  #print(tokens)#-------------------
#matriz de estados
matriz = [#   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27
          # dig, E/e, let,   >,   <,   +,   -,   =,   !,   /,   *,   %,   #,   .,   :,   {,   },   [,   ],   (,   ),   ;,   ,,   |,   &,   ',   ", esp
          [   1,  10,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,   0],# 0  ini
          [   1,   2, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,   5, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],# 1  dig
          [ 500, 500, 500, 500, 500,   3,   3, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 2  E/e
          [   4, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501],# 3  + -
          [   4, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201],# 4  dig
          [   6, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501],# 5    .
          [   6,   7, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202],# 6  dig
          [ 500, 500, 500, 500, 500,   8,   8, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],# 7  E/e
          [   9, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501, 501],# 8  + -
          [   9, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203],# 9  dig
          [  10,  10,  10, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204],# 10 let
          [ 205, 205, 205, 205, 205, 205, 205, 300, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205],# 11   >
          [ 206, 206, 206, 302, 206, 206, 206, 301, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206],# 12   <
          [ 207, 207, 207, 207, 207, 303, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207],# 13   +
          [ 208, 208, 208, 208, 208, 208, 304, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208],# 14   -
          [ 209, 209, 209, 209, 209, 209, 209, 305, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209, 209],# 15   =
          [ 210, 210, 210, 210, 210, 210, 210, 306, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210, 210],# 16   !
          [ 211, 211, 211, 211, 211, 211, 211, 211, 211, 307, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211, 211],# 17   /
          [ 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212, 212],# 18   *
          [ 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213, 213],# 19   %
          [ 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214, 214],# 20   #
          [ 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215, 215],# 21   .
          [ 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216, 216],# 22   :
          [ 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217, 217],# 23   {
          [ 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218, 218],# 24   }
          [ 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219],# 25   [
          [ 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220],# 26   ]
          [ 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221, 221],# 27   (
          [ 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222, 222],# 28   )
          [ 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223],# 29   ;
          [ 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224, 224],# 30   ,
          [ 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 502, 308, 502, 502, 502, 502],# 31   |
          [ 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 503, 309, 503, 503, 503],# 32   &
          [ 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225],# 33   '
          [ 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226, 226] # 34   "
         ]


def obtener_columna(charAscii):

  #detectar DÍGITOS
  if (charAscii >= 48 and charAscii <= 57):
    columna = 0

  #detectar E e
  elif (charAscii == 69 or charAscii == 101):
    columna = 1

  #detectar LETRAS
  #minúsculas y mayúsculas
  elif (charAscii >= 65 and charAscii <= 90 or charAscii >= 97 and charAscii <= 122):
    columna = 2

  #detectar > mayor que
  elif (charAscii == 62):
    columna = 3

  #detectar < menor que
  elif (charAscii == 60):
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

  #detectar !
  elif (charAscii == 33):
    columna = 8

  #detectar /
  elif (charAscii == 47):
    columna = 9

  #detectar *
  elif (charAscii == 42):
    columna = 10

  #detectar %
  elif (charAscii == 37):
    columna = 11

  #detectar #
  elif (charAscii == 35):
    columna = 12

  #detectar .
  elif (charAscii == 46):
    columna = 13

  #detectar :
  elif (charAscii == 58):
    columna = 14

  #detectar {
  elif (charAscii == 123):
    columna = 15

  #detectar }
  elif (charAscii == 125):
    columna = 16

  #detectar [
  elif (charAscii == 91):
    columna = 17

  #detectar ]
  elif (charAscii == 93):
    columna = 18

  #detectar (
  elif (charAscii == 40):
    columna = 19

  #detectar )
  elif (charAscii == 41):
    columna = 20

  #detectar ;
  elif (charAscii == 59):
    columna = 21

  #detectar ,
  elif (charAscii == 44):
    columna = 22

  #detectar |
  elif (charAscii == 124):
    columna = 23

  #detectar &
  elif (charAscii == 38):
    columna = 24

  #detectar '
  elif (charAscii == 39):
    columna = 25

  #detectar "
  elif (charAscii == 34):
    columna = 26

  #detectar si es NULL
  elif (charAscii == 32 or charAscii == 10 or charAscii == 13 or charAscii == 3 or charAscii == 0):
      columna = 27
  else:
    print("error caracter no reconocido" + str(charAscii))


  return columna

def obtener_resultado(edo, cadena_resultado):

  if edo == 0:
    print (cadena_resultado + "Estado: " + str(edo) + "Espacio" )
  if edo == 200:
    print( cadena_resultado + " Estado " + str(edo) + ": NúmeroEntero ")

  elif edo == 201:
    print( cadena_resultado + " Estado " + str(edo) + ": Número Entero Con Exponente ")

  elif edo == 202:
    print( cadena_resultado + " Estado " + str(edo) + ": Número Decimal ")

  elif edo == 203:
    print( cadena_resultado + " Estado " + str(edo) + ": Número Decimal Con Exponente ") #*******

  elif edo == 204:
    print( cadena_resultado + " Estado " + str(edo) + ": Identificador ") #regresar un espacio

  elif edo == 205:
    print( cadena_resultado + " Estado " + str(edo) + ": > ")

  elif edo == 206:
    print( cadena_resultado + " Estado " + str(edo) + ": < ")

  elif edo == 207:
    print( cadena_resultado + " Estado " + str(edo) + ": + ") #regresar un espacio

  elif edo == 208:
    print( cadena_resultado + " Estado " + str(edo) + ": - ")

  elif edo == 209:
    print( cadena_resultado + " Estado " + str(edo) + ": = ") #regresar un espacio

  elif edo == 210:
    print( cadena_resultado + " Estado " + str(edo) + ": ! ")

  elif edo == 211:
    print( cadena_resultado + " Estado " + str(edo) + ": / ") #regresar un espacio

  elif edo == 212:
    print( cadena_resultado + " Estado " + str(edo) + ": * ")

  elif edo == 213:
    print( cadena_resultado + " Estado " + str(edo) + ": % ") #regresar un espacio

  elif edo == 214:
    print( cadena_resultado + " Estado " + str(edo) + ": # ")

  elif edo == 215:
    print( cadena_resultado + " Estado " + str(edo) + ": . ") #regresar un espacio

  elif edo == 216:
    print( cadena_resultado + " Estado " + str(edo) + ": : ")

  elif edo == 217:
    print( cadena_resultado + " Estado " + str(edo) + ": { ") #regresar un espacio

  elif edo == 218:
    print( cadena_resultado + " Estado " + str(edo) + ": } ") #regresar un espacio

  elif edo == 219:
    print( cadena_resultado + " Estado " + str(edo) + ": [ ")

  elif edo == 220:
    print( cadena_resultado + " Estado " + str(edo) + ": ] ")

  elif edo == 221:
    print( cadena_resultado + " Estado " + str(edo) + ": ( ")

  elif edo == 222:
    print( cadena_resultado + " Estado " + str(edo) + ": ) ")

  elif edo == 223:
    print( cadena_resultado + " Estado " + str(edo) + ": ; ")

  elif edo == 224:
    print( cadena_resultado + " Estado " + str(edo) + ": , ")

  elif edo == 225:
    print( cadena_resultado + " Estado " + str(edo) + ": ' ")

  elif edo == 226:
    print( cadena_resultado + " Estado " + str(edo) + ": \" ")

  elif edo == 300:
    print( cadena_resultado + " Estado " + str(edo) + ": >= ")

  elif edo == 301:
    print( cadena_resultado + " Estado " + str(edo) + ": <= ")

  elif edo == 302:
    print( cadena_resultado + " Estado " + str(edo) + ": <> ")

  elif edo == 303:
    print( cadena_resultado + " Estado " + str(edo) + ": ++ ")

  elif edo == 304:
    print( cadena_resultado + " Estado " + str(edo) + ": -- ")

  elif edo == 305:
    print( cadena_resultado + " Estado " + str(edo) + ": == ")

  elif edo == 306:
    print( cadena_resultado + " Estado " + str(edo) + ": != ")

  elif edo == 307:
    print( cadena_resultado + " Estado " + str(edo) + ": // ")

  elif edo == 308:
    print( cadena_resultado + " Estado " + str(edo) + ": || ")

  elif edo == 309:
    print( cadena_resultado + " Estado " + str(edo) + ": && ")

  elif edo == 500:
    print( cadena_resultado + " Error " + str(edo) + ": Se esperaba un + o un -.")

  elif edo == 501:
    print( cadena_resultado + " Error " + str(edo) + ": Se esperaba un dígito.")

  elif edo == 502:
    print( cadena_resultado + " Error " + str(edo) + ": Se esperaba un |.")

  elif edo == 503:
    print( cadena_resultado + " Error " + str(edo) + ": Se esperaba un &.")

  elif edo == 504:
    print( cadena_resultado + " Error " + str(edo) + ": Caracter no reconocido.")
  else:
    print('caracter no Identificado ' + str(edo))

def retornar_lugar(edo):
  back = 0

  if (edo >= 200 and edo <= 226):
    back = 1

  return back

if __name__ == '__main__':
  main()
#Programa realizado por Maximiliano Garcia De Santiago
#Copyright (c) all rights reserved
#Contato [Facebook]:Max Garcia [Email]:max-gds96@hotmail.com
