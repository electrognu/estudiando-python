
def presentacion(param_lista):
    for i in range(0, len(param_lista)):
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





