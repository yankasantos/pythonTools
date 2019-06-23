height =float(input('Digite sual altura em metros:'))#convertendo  valor da altura em float
weight = float(input('Digite seu peso em Kg:'))#convertendo  valor do peso em float
imc = (weight//height ** 2) #Formula do IMC peso vezes altura ao quadrado... quando colocar // ele arredonda o valor
print(imc)