import streamlit as st
import pandas as pd
from PIL import Image

# Crea un diccionario y luego conviértelo en un DataFrame
table = pd.DataFrame({
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": [6, 7, 8, 9, 10]
})

# Muestra la tabla y el DataFrame
st.table(table)
st.dataframe(table)
# img = Image.open("imagen.png")
st.image("https://picsun.photos/200/300")


st.markdown("# Esto es un Titulo")
st.markdown("## Esto es codigo")
st.markdown("### Esto es codigo")
st.markdown("**Codigo** Prueba")
st.markdown("*Codigo* Prueba")
st.markdown("> Codigo Prueba")
st.markdown("1. Item\n 2. Item")
str= "print('Hello World')"
st.code(str)
st.markdown("_ _ _")
st.markdown('[Google](https://google.com)')
table = '''
# | Syntax | Description |
# | ----------- | ----------- |
# | Header | Title |
# | Paragraph | Text |

# '''
st.markdown(table)
json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)
st.metric(label='win speed',
          value='70 ms', delta='5.7')

st.markdown("That is so funny! :joy:")
