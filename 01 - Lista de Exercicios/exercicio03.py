valor = int(input("Digite um valor inteiro: "));

valores = [];
if((valor/1) > 0):
    valores.append("moedas de 1 real -> " + str(valor));

if((valor/2) > 0):
    valores.append("notas de 2 reais -> " + str(int(valor/2)));

if((valor/5) > 0):
    valores.append("notas de 5 reais -> " + str(int(valor/5)));

if((valor/10) > 0):
    valores.append("notas de 10 reais -> " + str(int(valor/10)));

if((valor/20) > 0):
    valores.append("notas de 20 reais -> " + str(int(valor/20)));

if((valor/50) > 0):
    valores.append("notas de 50 reais -> " + str(int(valor/50)));

if((valor/100) > 0):
    valores.append("notas de 100 reais -> " + str(int(valor/100)));

print(valores);