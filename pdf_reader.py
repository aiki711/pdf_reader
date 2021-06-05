import openpyxl
import tabula as tb
import pandas as pd
import streamlit as st
import io
import base64

st.title("pdf_reader")

uploaded_file = st.file_uploader("Choose an PDF file...", type="pdf")

if uploaded_file is not None:
    dfs = tb.read_pdf(uploaded_file, stream=True)
    df = pd.concat(dfs)

    towrite = io.BytesIO()
    uploaded_file = df.to_excel(towrite, encoding="utf-8", index=False, header=True)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    linko = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="myfilename.xlsx">Download excel file</a>'
    st.markdown(linko, unsafe_allow_html=True)
