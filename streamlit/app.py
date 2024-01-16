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
from chart import run_chart
from space import run_space
from PIL import Image
import base64

# python -m streamlit run app.py

df = pd.read_csv('C:/Users/ADMIN/Downloads/downlight.csv')
df2 = pd.read_csv('C:/Users/ADMIN/Downloads/indirect.csv')

def main():
    menu = ['홈','조명','단위공간']
    

    choice = st.sidebar.selectbox('Choose a menu',menu)
    
    if choice == '홈':
        st.subheader('Lighting Labs')
        st.write('조명 데이터 분석 및 제품 구매')
        img = Image.open("C:/Users/ADMIN/Desktop/home.png")
        st.image(img)

    elif choice == '조명':
        run_chart()
    
    elif choice == '단위공간':
        run_space()

if __name__ == '__main__' :
    main()
    