import streamlit as st
st.set_page_config(
    page_title='Mapa de estudos',
    page_icon='📖',
    layout='wide'
)
st.title('Estudos')
st.subheader('Registre seu conograma!')

st.sidebar.header('Seus Estudos')
horas = st.sidebar.slider('Horas de estudo',0,8,0)
pausas = st.sidebar.slider('Quantidade de pausas',0,8,0)
atividade = st.sidebar.selectbox('Tipo de estudo',{'Leitura', 'Exercício', 'Revisão'})

st.metric('Horas',f'{horas} de estudo')
st.metric('Quantidade',f'{pausas} de pausas')
st.metric('Com', atividade)

col1, col2, col3 = st.columns(3)
with col1:
    st.header('Detalhes do estudo')
    st.write('Você Estudou bem!' if horas >= 2 else 'Está estudando pouco...')
with col2:
    st.header('Pausas')
    st.write('Bom, Você faz boas pausas!' if pausas >= 4 else 'Você fazer mais pausas...')
with col3:
    st.header('Exercício')
    if atividade == 'Leitura':
        st.write('Estás estudando lendo, Bom!')
    elif atividade == 'Exercícios':
        st.write('Estás estudando praticando, Bom!')
    elif atividade == 'Revisão':
        st.write('Estás estudando revendo')
    else:
        st.write('ERRO#') 
with st.expander('Dicas rápidas'):
    st.write('- Estude por duas horas')
    st.write('- tenha pelo menos 4 pausas nesse tempo')
    st.write('- A revisão é somente depois da leitura(teoria) e exercício(pratica)')
st.markdown('---')
st.markdown(' Projeto com Streamlit ')