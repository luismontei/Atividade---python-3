print("calcular quantidade de numeros impares e pares")
par=0
impar=0
for i in range(5):
    numero = int(input(" digite um numero: "))
    if(numero%2==0):
         par=par+1
    else:
        impar=impar+1
print("Números pares {}".format(par))
print("Números impares {}".format(impar))
