from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import joblib
import streamlit as st
import time
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image

df = pd.read_csv('C:/Users/ADMIN/Downloads/downlight.csv')
df2 = pd.read_csv('C:/Users/ADMIN/Downloads/indirect.csv')
def run_chart():
    
    st.subheader('조명 데이터 분석')
    select = st.selectbox('조명선택:',('다운라이트','간접조명'))
    
    if select == '다운라이트':
        bin_width = 1000
        fig1 = px.histogram(df, x='price', nbins=int((df['price'].max() - df['price'].min()) / bin_width),
                   range_x=[df['price'].min(), df['price'].max()],
                   title='다운라이트 조명 가격 분포',
                   labels={'price': '가격', 'count': '제품수'})
        st.plotly_chart(fig1)
        st.caption('단위 : 1000won')
    
        
        describe1 =  df['price'].describe()
        st.write(describe1)
        
    elif select == '간접조명':
        bin_width = 1000
        fig2 = px.histogram(df2, x='price', nbins=int((df2['price'].max() - df2['price'].min()) / bin_width),
                   range_x=[df2['price'].min(), df2['price'].max()],
                   title='간접조명 가격 분포',
                   labels={'price': '가격', 'count': '제품수'})
        st.plotly_chart(fig2)
        st.caption('단위 : 1000won')
        
        describe2 =  df2['price'].describe()
        st.write(describe2)        