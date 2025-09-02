import streamlit as st
st.set_page_config(
    page_title="Hábitos Melhores",
    page_icon="",
    layout='wide'
)

st.title('Hábitos Melhores')
st.subheader('Registre e visualize suas hábitos diários')
st.sidebar.header('Seus hábitos')

sono = st.sidebar.slider('Horas de sono',0,12,8)
agua = st.sidebar.slider('Copos de água',0,10,5)
exercicio = st.sidebar.selectbox('Exercécio', ['Nenhum','Leve','Moderado','Intenso'])

st.metric('Sono',f'{sono} horas')
st.metric('Água',f'{agua} copos')
st.metric('Exercício', exercicio)

col1, col2, col3 = st.columns(3)
with col1:
    st.header('Detalhes do sono')
    st.write('Você dormiu bem!' if sono >= 7 else 'tente dormir mais...')
with col2:
    st.header('Hidratação')
    st.write('Bom, Você está hidratado' if agua >= 6 else 'Você deve beber mais água')
with col3:
    st.header('Exercício')
    st.write('Tu está indo bem!' if exercicio != 'Nenhum' else 'Você deve fazer mais exercício')

with st.expander('Dicas rápidas'):
    st.write('- Durma pelo menos 7 horas')
    st.write('- Beba pelo menos 6 copos de água')
    st.write('- Fique ativo, em relação a exercício/movimento, pelo menos uma vez por dia')
st.markdown('---')
st.markdown(' Projeto com Streamlit ')