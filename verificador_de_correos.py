txt = input("ingrese un curreo: ")

if "@" in txt and ".com" in txt and txt.index("@") < txt.index(".com"):
    print("Correcto")

else:
    print("Incorrecto")