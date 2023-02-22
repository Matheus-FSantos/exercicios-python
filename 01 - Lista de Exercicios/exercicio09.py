import random

valores = [];
aux = 0;

for i in range(10):
    valores.append(random.randint(1, 100));

for i in range(len(valores)):
    for l in range(len(valores)):
        if(valores[l] > valores[i]):
            aux = valores[i];
            valores[i] = valores[l];
            valores[l] = aux;

print(valores);