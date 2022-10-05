import streamlit as st

from steps import step1
from steps import step2
from steps import step3

# Make the page wide to fit the table
st.set_page_config(layout="wide")

# The code below is for the top markup
st.title('Lista de precios HG')

# Code to handle the excel upload
step1.upload_file()

if step1.is_file_uploaded():
  step2.show_all_products()

else:
    step1.reset()
    st.stop()

if step2.are_products_selected():
  step3.show_form()

else:
    step2.reset()
    st.stop()

if step3.is_form_submitted():
  print(st.session_state.invoice_information)

else:
    step3.reset()
    st.stop()