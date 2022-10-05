import streamlit as st
from fpdf import FPDF

def generate_invoice():
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font('Arial', 'B', 16)
  pdf.cell(40, 10, 'Cumbia')
    
  st.download_button(
    "Descargar remito",
    data=pdf.output(dest="S").encode("latin-1"),
    file_name="remito.pdf"
  )