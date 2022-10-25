#print('''hola mundo''')

edadDePerro = input("Cuantos años tiene tu perro?: ")

def calcularEdadDePerros (edadDePerro): 
    TEXTO = ("La edad de tu mascota es: ")
    CALCULO = int(edadDePerro) * 4 + 20
    RESULTADO = str(CALCULO)
    print(" ")
    print("....................")
    print(TEXTO + RESULTADO)
    print("....................")
    print(" ")

calcularEdadDePerros(edadDePerro)


