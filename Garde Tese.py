# %%
#Grade de Coleta
import datetime
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from  PIL import Image
import io 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import streamlit_nested_layout

public_gsheets_url = pd.read_excel("https://docs.google.com/spreadsheets/d/1iQvoFAM3FvpNaR9HPyidDUm5jtMehwSykcITOCRby_c/export?format=xlsx",sheet_name="D0 Dados")

# %%
st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Tubo de Expedição </p>', unsafe_allow_html=True)
# %%
#st.set_page_config(layout='wide') #Choose wide mode as the default setting
#Add a logo (optional) in the sidebar
logo = Image.open(r"C:\Users\luan.carvalho\Solistica\Torre de Controle - Transportes WHS-BR - Diretório_Operacionais\PROCESSOS E SISTEMAS\LOGOS SOLISTICA IMAGENS\Elemento-Logo.png")
st.sidebar.image(logo,  width=100)
#add_selectbox = st.sidebar.selectbox("How would you like to be contacted?",
    #(public_gsheets_url['Modal'].unique()))
    
# with st.sidebar.form(key='columns_in_form',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
#     st.write('Please help us improve!')
#     st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True) #Make horizontal radio buttons
#     rating=st.radio("Please rate the app",('1','2','3','4','5'),index=4)    #Use radio buttons for ratings
#     text=st.text_input(label='Please leave your feedback here') #Collect user feedback
#     submitted = st.form_submit_button('Submit')
# %%
#st.title('Tubo De Expedição/Produção')
public_gsheets_url = public_gsheets_url.drop(['Data','Hora','Volume'],axis=1)
Index_o= ['Planilha','Veículo','Modal','Trans','GRADE DE COLETA','Secos','Inflamável','Biológico','Climatizado','Aftosa','Volumes']
public_gsheets_url= public_gsheets_url.fillna("")
# pr = public_gsheets_url.profile_report()
# st_profile_report(pr)
if st.checkbox('Mostrar dados brutos'):
    st.subheader('Tubo Completo')
    st.dataframe(public_gsheets_url[Index_o])
#%%
st.bar_chart(public_gsheets_url,x='Veículo',y='Secos')
# %%]
