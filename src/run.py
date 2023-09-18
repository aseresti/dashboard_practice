import streamlit as st
from io import StringIO
import json

st.title("My First DashBoard")
st.text('Hi')
st.code("x = 12")
upload_file = st.file_uploader("Choose a File")
if upload_file is not None:
    # To convert to a string based IO
    stringio = StringIO(upload_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data)
    data = json.loads(string_data)
    st.json(data)
    