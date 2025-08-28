import streamlit as st

#---------------------------------SIDEBAR
st.sidebar.image('Logo.png')
st.sidebar.title('VivaBem - Fitness & Bem-Estar')

nome = st.sidebar.text_input('Qual o seu nome? ')
idade = st.sidebar.text_input('Qual a sua idade? ')
peso = st.sidebar.text_input('Qual é o seu peso? ')
altura = st.sidebar.text_input('Qual é a sua altura? ')


#PRINCIPAL-------------------------------------------
st.markdown(f'##### IMC:CONHEÇA SEU CORPO, CUIDE DA SUA SAÚDE. ')


st.markdown('''| Faixa de IMC        | Classificação                  |
|---------------------|-------------------------------|
| < 18.5              | Abaixo do peso                 |
| 18.5 – 24.9         | Peso normal                    |
| 25.0 – 29.9         | Sobrepeso                      |
| 30.0 – 34.9         | Obesidade Grau I               |
| 35.0 – 39.9         | Obesidade Grau II              |
| ≥ 40.0              | Obesidade Grau III (mórbida)   |''')

if st.sidebar.button('Calcular '):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura**2)    
    st.metric('IMC', imc)

    if imc <=18.5:
        st.warning(f'{nome}, você está abaixo do peso. É importante cuidar disso para evitar problemas de saúde.')
    elif imc <=24.9:
        st.warning(f'{nome}, seu peso está dentro do normal. Continue cuidando da saúde. ')
    elif imc <=29.9:
        st.warning(f'{nome}, você está com sobrepeso. É importante cuidar disso para evitar riscos á saúde. ')
    elif imc <=34.9:
        st.warning(f'{nome}, você está com obesidade grau I. Isso exige atenção para prevenir complicações de saúde. ')
    elif imc <=39.9:
        st.warning(f'{nome}, seu resultado indica obesidade grau II. Isso exige atenção e acompanhamento. ')
    else:
        st.warning(f'{nome}, o resultado mostra obesidade grau III, o que representa um risco importante para a saúde. ')