# Laboratorio de Fisica Computacional
# Joselyn Quispe

def MRU():

    opcion = int(input("Variable que desea encontrar: \n1) x (distancia)\n2) v (velocidad)\n3) t (tiempo)\n> "))

    res = 0

    if opcion == 1:

        v = float(input("v: "))
        t = float(input("t: "))

        res = v * t

        print("Resultado x: ", res, "\n")

    elif opcion == 2:

        x = float(input("x: "))
        t = float(input("t: "))

        if (t != 0):
            res = x / t
            print("Resultado v: ", res, "\n")
        else:
            print("error")

    elif opcion == 3:

        x = float(input("x: "))
        v = float(input("t: "))

        if (v != 0):
            res = x / v
            print("Resultado t: ", res, "\n")
        else:
            print("error")


def MRUV():

    opcion = int(input("Variable que desea encontrar: \n1) x (distancia)\n2) a (aceleracion)\n"
                       "3) t (tiempo)\n4) vi (velocidad inicial)\n5) vf (velocidad final)\n> "))

    if opcion == 1:

        vi = float(input("vi: "))
        t = float(input("t: "))
        a = float(input("a: "))

        res = vi * t
        res += (a * t * t) / 2
        print("resultado x: ", res, "\n")

    elif opcion == 2:

        vi = float(input("vi: "))
        t = float(input("t: "))

        if t != 0:

            varFinal = int(input("Como ultima varible tiene ¿x o vf?: \n1) x (distancia) \n2) vf (velocidad final) \n>"))

            if varFinal == 1:

                x = float(input("x: "))

                aux = vi * t
                res = x - aux
                res *= 2
                res /= (t * t)
                print("resultado a: ", res, "\n")

            elif varFinal == 2:

                vf = float(input("vf: "))

                aux = vi * t
                res = (vf - aux)
                res /= t
                print("resultado a: ", res, "\n")

        else:
            print("error")

    elif opcion == 3:

        vi = float(input("vi: "))
        a = float(input("a: "))
        vf = float(input("vf: "))

        res = vf
        res /= (vi + a)
        print("resultado t: ", res, "\n")

    elif opcion == 4:

        a = int(input("a: "))
        t = int(input("t: "))

        if t != 0:

            varFinal = int(input("Como ultima varible tiene ¿x o vf?: \n1) x (distancia) \n2) vf (velocidad final) \n>"))

            if varFinal == 1:

                x = float(input("x: "))
                res = 2 * x
                aux = a * t * t
                aux = res - aux
                res = aux / (2 * t)
                print("resultado vi: ", res, "\n")

            elif varFinal == 2:

                vf = float(input("vf: "))

                aux = a * t
                res = vf - aux
                res /= t
                print("resultado vi: ", res, "\n")

        else:
            print("error")

    elif opcion == 5:

        vi = float(input("vi: "))
        a = float(input("a: "))
        t = float(input("t: "))

        res = vi * t
        res += a * t
        print("resultado vf: ", res, "\n")


while True:

    opcion = int(input("Elige el tipo de problema:\n1) MRU  \n2) MRUV\n>"))

    if opcion == 1:
        MRU()

    elif opcion == 2:
        MRUV()

    else:
        print("No valido")