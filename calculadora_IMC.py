
print("CALCULADORA IMC version 1.0")

def calcularIMC(peso,altura):
    imc = peso/(altura * altura)
    return imc

def pedirELIMC():

    peso = float(input("ingrese su peso en kg:  "))
    alturaEnCM = int(input("ingrese se altura en cm: "))
    alturaEnMetros = alturaEnCM / 100
    imc = peso / (alturaEnMetros * alturaEnMetros)


    print("Su IMC es de " + str(imc))


    if imc < 20:
        print("Está delgado")
    if imc >= 20 and imc < 30:
        print("Está en un peso normal")
    if imc >= 30:
        print("Está con obesidad,cuidado!")
        print("Su IMC es de : " + str(imc))

print("Bienvenido a el calculador de IMC")
pedirELIMC()
