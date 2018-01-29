# -*- coding: utf-8 -*-
def derivador():
   print("Esto es el modulo de preguntas")
   deriv = int(input("Introduce el numero de referencia del derivador: 80998, 79797. Si introduce 0 podra escribir todos los datos manualmente"))
   if deriv == 80998:
       print("El número de referencia del derivador elegido es 80998")
       perd_deriv = 5
       print("Las perdidas por derivacion del derivador elegido son", perd_deriv)
       perd_inser = 12
       print("Las perdidas por insercion del derivador elegido son", perd_inser)

   if deriv == 79797:
       print("El numero de referencia del derivador elegido es 79797")
       perd_deriv = 8
       print("Las perdidas por derivacion del derivador elegido son", perd_deriv)
       perd_inser = 15
       print("Las perdidas por insercion del derivador elegido son", perd_inser)

   if deriv == 0:
       perd_deriv = int(input("Introduce las perdidas por derivacion"))
       print("Las perdidas por derivacion son", perd_deriv)
       perd_inser = int(input("Introduce las perdidas por insercion"))
       print("Las perdidas por insercion son", perd_inser)

   return (perd_deriv,perd_inser)


def Pau_repartidor():
   pau = int(input("Introduce el numero de referencia del pau repartidor: 5154 (conectores tipo F), 544902 (conexion brida). Si introduce 0 podra escribir todos los datos manualmente"))
   if pau == 5154:
       perd_pau_repartidor = 7.5
       print("Las perdidas del pau repartidor son", perd_pau_repartidor)

   if pau == 544902:
       perd_pau_repartidor = 9
       print("Las perdidas del pau repartidor son", perd_pau_repartidor)

   if pau == 0:
       perd_pau_repartidor = int(input("Introduce las perdidas del pau repartidor"))
       print("Las perdidas del pau repartidor son", perd_pau_repartidor)

   return(perd_pau_repartidor)

def Toma():
   toma = int(input("Introduce el numero de referencia de la toma: 5226, 524501. Si introduce 0 podra escribir todos los datos manualmente"))
   if toma == 5226:
       perd_toma = 1.5
       print("Las perdidas de la toma son", perd_toma)

   if toma ==
   if toma == 0:
       perd_toma = int(input("Introduce las perdidas de la toma"))
       print("Las perdidas de la toma son", perd_toma)

   return(perd_toma)

def Mezclador():
   mezclador = int(input("Introduce el numero de referencia del mezclador: 7407, 7452. Si introduce 0 podra escribir todos los datos manualmente"))
   if mezclador == 0:
       perd_insercion_mezclador = int(input("Introduce las perdidas por derivacion del mezclador"))
       print("Las perdidas por derivacion del mezclador son", perd_insercion_mezclador)

   return(perd_insercion_mezclador)

def Amplificador():
   amplificador = int(input("Introduce el numero de referencia del amplificador:. Si introduce 0 podra escribir todos los datos manualmente"))
   if amplificador == 0:
       ganancia = int(input("Introduce la ganancia del amplificador"))
       print("La ganancia del amplificador es", ganancia)
       figura_de_ruido = int(input("Introduce la figura de ruido del amplificador"))
       print("La figura de ruido del amplificador es", figura_de_ruido)
   return (ganancia, figura_de_ruido)

