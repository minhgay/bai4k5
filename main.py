import streamlit as st
import pandas as pd
csv_content = '''Mien,San_luong,Nam,Don_vi_tinh
Nord,150000,2025,tones
Central,10000,2025,tones
South,200000,2025,tones
'''
with open('pro5.4.csv','w',encoding='utf-8') as f:
    f.write(csv_content)
df = pd.read_csv('pro5.4.csv')
st.subheader('Bảng DL gốc:')
st.dataframe(df)
st.title('sản lượng lúa thu hoạch 3 miền năm 2025')
df_chart= pd.DataFrame({
    'category':df['Mien'],
    'value':df['San_luong'],
    'order':[1,2,3]
})
st.subheader('round chart')
st.vega_lite_chart(
df_chart,
{
    'mark': {'type':'arc'},
    'encoding':{
        'theta':{'field':'value', 'type':'quantitative',
                 'scale':{'range': [2.35619, 8.63937]}        },
        'color':{
            'field':'category',
            'type':'nominal',
            'scale':{
                'domain':['Nord','Central','South'],
                'range':["#416D9D", "#674028", "#DEAC58"]
            },
            'legend':{'title':'Miền'}
        },
        'order': {'field': 'order'}
    }
}
)
