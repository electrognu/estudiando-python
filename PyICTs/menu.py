#!/usr/bin/python3
# -*- coding: utf-8 -*-
from modulopregunta import *



nele = input("numero de elementos que hay: ")

atc = input("cual sera la atenuacion del cable: ")


print "----------------------------------------------------"
print "1.-derivador        2.-pau        3.-cable"

print "----------------------------------------------------"
print "4.-toma            5.-mezclador       6.-antena"


x = 0
while x < nele:
    
           
    print 'introduce el elemento', x,':'
    opcion = int(input())
            
          

    if opcion == 1:
       
        pd,pi = derivador()
        derivador1 = input("introduce el tipo de derivador: ")
        derivador2 = input("introduce cuantos derivadores hay: ")
               

    if opcion == 2:
        pd = pau()
        pau1 = input("introduce el tipo de pau: ")
        pau2 = input("introduce cuantos paus hay: ")
                
            

    if opcion == 3:
        pi = mezclador()
        cable1 = input("Introduce el tipo de cable: ")
        cable2 = input("Introduce cuantos cables hay: ")
                
            
    if opcion == 4:
        pd = toma()
        toma1 = input("Introduce el tipo de toma: ")
        toma2 = input("Introduce cuantas tomas hay: ")    
                
                
    if opcion == 5:
        mezclador1 = input("introduce el tipo de mezclador: ")
        mezclador2 = input("introduce cuantos mezcladores hay: ")
                
                
    if opcion == 6:
        antena = input("introduce el tipo de antena: ")    
            
    x = x + 1   
                
                
                
                
         
        
