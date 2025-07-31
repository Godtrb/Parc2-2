def Euclid(a,b):
    print(f"MCD({a}, {b})")

    if b==0:
        return a
    else:
        r = divmod(a,b)
        r=r[1]
        a = b
        return Euclid(a,r)
def RepText(a,b):
    if b==0:
        return
    else:
        print(a)
        return RepText(a,b-1)
def DigCont(a,b=1):
    x=pow(10,b)
    if x>a:
        return b
    else:
        return DigCont(a,b+1)
def ContLetra(a,pal,len,cont=0):
    if len==0:
        return cont
    else:
        if pal[len-1]==a:
            cont+=1
            return ContLetra(a,pal,len-1,cont)
        else:
            return ContLetra(a,pal,len-1,cont)
def BinTurn(a,binlen=1):
    lenght=pow(2,binlen)
    if lenght<=a:
        return BinTurn(a,binlen+1)
    elif lenght>=a:
        return BinTurn(a,lenght-1)



while e!=6:
    print("------Menu Recursivo--------")
    print("1.MCD")
    print("2.Rep un texto varias veces")
    print("3.Contar digitos de un numero")
    print("4.Contar letras en una palabra")
    print("5.Convertir a binario")
    print("6.Exit")
    e=int(input())
    match e:
        case 1:
            firstimp = int(input("Ingrese el primer numero: "))
            secondimp = int(input("Ingrese el segundo numero: "))
            print(f"El MCD es {Euclid(firstimp, secondimp)} ")
        case 2:
            text = input("Ingrese texto: ")
            Reps = int(input("ingrese el numero de veces a repetir el texto "))
            RepText(text, Reps)
        case 3:
            numdigs = int(input("Enter number: "))
            print(f"el numero ingresado tiene {DigCont(numdigs)} digitos")
        case 4:
            palreq = input("Ingrese palabra: ")
            letra = input("Ingrese letra: ")
            lenght = len(palreq)
            print(f"La letra {letra} se repite {ContLetra(letra, palreq, lenght)} veces")
