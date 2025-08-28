
print('| ---------------------------------------------------- |')
print('| IMC: CONHEÇA SEU CORPO, CUIDE DE SUA SAÚDE           |')
print('| ---------------------------------------------------- |')
print('| Faixa de IMC        | Classificação                  |')
print('|---------------------|------------------------------- |')
print('| < 18.5              | Abaixo do peso                 |')
print('| 18.5 – 24.9         | Peso normal                    |')
print('| 25.0 – 29.9         | Sobrepeso                      |')
print('| 30.0 – 34.9         | Obesidade Grau I               |')
print('| 35.0 – 39.9         | Obesidade Grau II              |')
print('| ≥ 40.0              | Obesidade Grau III (mórbida)   |')
print('| ---------------------------------------------------- |')
nome = input('Qual o seu nome? ')
int(input('Qual a sua idade? '))
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual é sua altura? '))



imc = peso / (altura**2)

if imc <=18.5:
    print(f'{nome}, você está abaixo do peso. É importante cuidar disso para evitar problemas de saúde.')
elif imc <=24.9:
    print(f'{nome}, seu peso está dentro do normal. Continue cuidando da saúde. ')
elif imc <=29.9:
    print(f'{nome}, você está com sobrepeso. É importante cuidar disso para evitar riscos á saúde. ')
elif imc <=34.9:
    print(f'{nome}, você está com obesidade grau I. Isso exige atenção para prevenir complicações de saúde. ')
elif imc <=39.9:
    print(f'{nome}, seu resultado indica obesidade grau II. Isso exige atenção e acompanhamento. ')
else:
    print(f'{nome}, o resultado mostra obesidade grau III, o que representa um risco importante para a saúde. ')