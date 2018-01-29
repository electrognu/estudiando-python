#!/usr/bin/python3
# -*- coding: utf-8 -*-
from modulopregunta import *

Lista = [] # Lista de elementos 

nele = input("numero de elementos que hay: ")

atc = input("cual sera la atenuacion del cable: ")

def menu():
	print ("----------------------------------------------------")
	print ("--------------------- MENU -------------------------")
	print ("----------------------------------------------------")
	print ("1.-derivador        2.-pau        3.-cable")
	print ("----------------------------------------------------")
	print ("4.-toma            5.-mezclador       6.-antena")
	print ("----------------------------------------------------")


x = 0
while x < nele:
    
    menu()       
    print ('Introduce el elemento', x,':')
    opcion = int(input())
       
          

    if opcion == 1:
       
        pd,pi = derivador()
        Lista.append(["Derivador",pd,pi])
               

    if opcion == 2:
        pd = pau()
        Lista.append(["Pau",pd])
                
            

    if opcion == 3:
	    print(" Esta opcion no funciona todavia ")
    if opcion == 4:
        pd = toma()
        Lista.append(["Toma",pd])
               
    if opcion == 5:
	    pi = mezclador()
		Lista.append(["Mezclador",pi])
                        
    if opcion == 6:
        antena = input("introduce el tipo de antena: ")    
            
    x = x + 1   
                
for i in range(0, len(Lista)):
    lista2 = Lista[i]
    if lista2[0] == 'Amplificador'or lista2[0] == 'amplificador':
        print(i+1,":",lista2[0],".G:",lista2[1],"\t\t   .F:",lista2[2])
    elif lista2[0] == 'Mezclador'or lista2[0] == 'mezclador':
        print(i + 1, ":", lista2[0], "   .Perdida:", lista2[1])
    elif lista2[0] == 'derivador'or lista2[0] == 'Derivador':
        print(i + 1, ":", lista2[0], "   .Perdida paso", lista2[1], ".Perdida derivacion", lista2[2])
    elif lista2[0] == 'PAU':
        print(i + 1, ":", lista2[0], "\t\t .Perdida ", lista2[1])
    elif lista2[0] == 'toma' or lista2[0] == 'Toma':
        print(i + 1, ":", lista2[0], "\t\t .Perdida ", lista2[1])              
                
                
         
        
