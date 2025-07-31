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
def ContLetra(a,):
x="ran"
print(x[1])
e=0
match e:
    case 1:
        firstimp=int(input("Enter first number: "))
        secondimp=int(input("Enter second number: "))
        print(f"El MCD es {Euclid(firstimp,secondimp)} ")
    case 2:
        text=input("Enter text: ")
        Reps=int(input("Enter number of times youd like the text to repeat: "))
        RepText(text,Reps)
    case 3:
        numdigs=int(input("Enter number: "))
        print(f"el numero ingresado tiene {DigCont(numdigs)} digitos")
while e!=5:
    print("------Menu Recursivo--------")
    print("1.MCD")
    print("2.Rep un texto varias veces")