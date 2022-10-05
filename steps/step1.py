import streamlit as st
import pandas as pd

def upload_file():
  uploaded_file = st.file_uploader("Subir archivo XLS 👇🏻", accept_multiple_files=False)

  # Product codes to look for
  products = []
  codes = ["BLB010", "BLB020", "BLB030", "BLB040", "BLB050", "BLB070", "BLB110", "BLB130", "BLB135B", "BC050", "BC070", "TCL40", "DIC18", "PDE01", "PDE02", "PDE03", "PDE04", "PDE05", "PDE06", "PDE07", "PDE24", "PDE26", "PDE28", "PDE31", "PDE34", "PDE36", "PDD1", "PDD2", "PDD3", "PDD4", "PDD5", "PDD6", "PDDR0", "PDDR1", "PDDR3", "PDDR5", "PDDR6", "BEPT2L", "BEPT3L", "BEPT4A", "BEPT5", "BEPT6L", "BEPT7", "KM12", "KM21", "BC25A", "BC30A", "PZP1", "PZP2", "PZP3", "BA2030B", "BA4060B", "BCA411B", "BCA561B", "FL6", "FL7", "BPP2030", "BPP2535", "BPP3040", "BPP3545", "CBO1", "CBO2", "CBO3", "CBO4", "BP", "BS901", "BS902", "KI", "CAP241", "CP02", "ML14", "BR8", "BR4", "F076", "R16", "BME102", "BME103", "BME105OV", "BME107", "PP223K1", "PP223K2", "BBB10", "BBB13", "BBB15", "BBB18", "BBB20", "BBB23", "BBB24", "BBB26", "BBB28", "BBB30", "BBB32", "BBB34", "BBB36", "BBB38", "BBB40", "BBBR1825", "BBBR2127", "BBBR2632", "BBBR3137", "BBBR3545", "BBBR4050", "BBBR4555", "PIR04", "PIR05", "PIR06", "PIR07", "PIR08", "PIR10", "PIRP4", "V46"]

  # Function to get the necessary data from the excel file
  if uploaded_file:
    try:
      excel = pd.read_excel(uploaded_file)
      
      for code in codes:
        product = excel[excel["Unnamed: 0"] == code]
        products.append([
          # Quantity
          "1",
          # Code
          product["Unnamed: 0"].values[0],
          # Description
          product["Unnamed: 1"].values[0],
          # Initial Price
          product["Unnamed: 2"].values[0],
          # Final price
          round(product["Unnamed: 2"].values[0] + product["Unnamed: 2"].values[0] * 50 / 100),
        ])

        if 'products' not in st.session_state:
          st.session_state.all_products = products
      
    except:
      st.error('Por favor, subí un archivo Excel válido')
      st.stop()

def is_file_uploaded():
  return 'all_products' in st.session_state

def reset():
  if 'all_products' in st.session_state:
    del st.session_state.all_products