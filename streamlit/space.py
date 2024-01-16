from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import streamlit as st
import time
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
import base64
def run_space():
    st.subheader('단위공간별 정보')
    
    selected_space = st.radio('select the place : ', ('침실', '거실', '주차장' , '카페'))
    st.write(selected_space,'을 선택하셨습니다.', selected_space, '공간에 대한 사진과 가격 정보입니다.' )
    
    if selected_space == '침실' :
        with st.expander( "see photo, click + "):
                
                #img = Image.open('C:/Users/ADMIN/Desktop/IOT2.gif') 
                #st.image(img)
                #st.write(selected_space, """IOT제어 냉난방연동""")    
                
                file = open("C:/Users/ADMIN/Desktop/IOT2-ezgif.com-resize.gif", "rb") 
                contents = file.read()
                data_url = base64.b64encode(contents).decode("utf-8")
                file.close()
                st.markdown(
                    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                    unsafe_allow_html=True,)

                
                



                                
                
