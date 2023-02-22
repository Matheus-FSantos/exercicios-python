def fatorial(valor):
    if(valor == 1):
        return valor;
    else:
        return valor * fatorial(valor - 1);


numero = int(input("Informe um valor: "));
valor = fatorial(numero);

print(valor);