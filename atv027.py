primeiro = int(input("digite o primeiro do intervalo: "))
ultimo = int(input("digite o ultimo do intervalo: "))
soma=0
while (primeiro < ultimo - 1):
    primeiro = primeiro+ 1
    print(primeiro)
    soma = (primeiro+soma)

print("a soma dos intervalos é = {}".format(soma))