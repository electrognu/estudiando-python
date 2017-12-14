


lista1 = []
nelem = int(input("Numero elem?"))

for i in range (0, nelem):
    tipo = input("Tipo:")
    if tipo == 'amplificador' or tipo == 'Amplificador':
        valor1 = float(input("Ganancia"))
        valor2 = float(input("Figura Ruido"))
        lista1.append([tipo, valor1, valor2])
    elif tipo == 'Mezclador' or tipo == 'mezclador':
        valor1 = float(input("Perdida de inserción:"))
        lista1.append([tipo,valor1])
    elif tipo == 'derivador' or tipo == 'Derivador':
        valor1 = float(input("Perdidas de paso:"))
        valor2 = float(input("Perdidas de derivacion"))
        lista1.append([tipo,valor1,valor2])
    elif tipo == 'PAU':
        valor1 = float(input("Atenuacion:"))
        lista1.append([tipo,valor1])
    elif tipo == 'toma' or tipo == 'Toma':
        valor1 = float(input("Atenuacion"))
        lista1.append([tipo,valor1])

for i in range(0, len(lista1)):
    lista2 = lista1[i]
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





