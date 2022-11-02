import streamlit as st
from fpdf import FPDF
import time

class PDF(FPDF):
  def header(self):
    today = time.strftime("%d/%m/%Y")

    # First row
    self.set_font('Arial', '', 8)
    self.cell(63, 10, 'Envio:', 1, 0, 'C')
    self.set_font('Arial', 'B', 15)
    self.cell(63, 10, 'Remito "X"', 1, 0, 'C')
    self.set_font('Arial', '', 8)
    self.cell(63, 10, 'Papelera HG', 1, 0, 'C')
    # Line break
    self.ln(10)
    # Second row
    self.set_font('Arial', '', 8)
    self.cell(63, 10, f"Fecha: {today}", 1, 0, 'C')
    self.set_font('Arial', '', 8)
    self.cell(63, 10, 'Traslado mercaderías', 1, 0, 'C')
    self.set_font('Arial', '', 8)
    self.cell(63, 10, 'Original', 1, 0, 'C')
    # Line break
    self.ln(10)
    # Third row
    self.set_font('Arial', '', 8)
    self.cell(63, 20, "No válido como factura", 1, 0, 'C')
    self.set_font('Arial', '', 8)
    self.cell(63, 20, 'Se adjuntan facturas Originales', 1, 0, 'C')
    self.set_font('Arial', '', 8)
    self.cell(63, 20, f"Facturas: {st.session_state.invoice_information[0]}", 1, 0, 'C')
    # Line break
    self.ln(20)
    # Quantity and description
    self.set_font('Arial', 'B', 8)
    self.cell(64, 10, 'Cantidad:', 0, 0)
    self.cell(120, 10, 'Descripción:', 0, 0)
    self.ln(10)
    self.line(10, 60, 199, 60)
    self.ln(2)
  
  def footer(self):
    self.set_y(-80)
    self.set_font('Arial', '', 8)
    # First row
    self.line(10, 223, 199, 223)
    self.cell(63, 20, "De: García Horacio C.", 0, 0)
    self.cell(63, 20, "Recibe:", 0, 0)
    self.ln(4)
    self.cell(63, 20, "General Paz 1642", 0, 0)
    self.cell(63, 20, st.session_state.invoice_information[1], 0, 0)
    self.ln(4)
    self.cell(63, 20, "Bragado - Buenos Aires", 0, 0)
    self.ln(4)
    self.cell(63, 20, "CUIT: 20268659766", 0, 0)
    self.ln(4)
    self.cell(63, 20, "IVA: Responsable Monotributo", 0, 0)
    self.ln(8)
    # Second row
    self.line(10, 247, 199, 247)
    self.cell(63, 20, "Enviar por:", 0, 0)
    self.cell(63, 20, st.session_state.invoice_information[2], 0, 0)
    self.ln(8)
    # Third row
    self.line(10, 255, 199, 255)
    self.cell(63, 20, "Teléfono:", 0, 0)
    self.cell(63, 20, st.session_state.invoice_information[3], 0, 0)
    self.ln(8)
    # Fourth row
    self.line(10, 263, 199, 263)
    self.cell(63, 20, "Valor seguro:", 0, 0)
    self.cell(63, 20, f"${st.session_state.invoice_information[4]}", 0, 0)
    self.ln(8)
    # Fifth row
    self.line(10, 271, 199, 271)
    self.cell(63, 20, "Fecha despacho:", 0, 0)
    self.cell(63, 20, "Bultos:", 0, 0)
    self.ln(8)
    # Sixth row
    self.line(10, 279, 199, 279)
    self.cell(63, 20, "Observaciones:", 0, 0)

def generate_invoice():
  pdf = PDF()
  pdf.alias_nb_pages()
  pdf.add_page()
  pdf.set_font('Arial', '', 8)

  # Products content
  products = st.session_state.selected_products
  for i in range(len(products)):
    print(products[i])
    pdf.cell(64, 5, products[i]["Cantidad"], 0, 0)
    pdf.cell(120, 5, products[i]["Descripción"], 0, 0)
    pdf.ln(5)
    
  st.download_button(
    "Descargar remito",
    data=pdf.output(dest="S").encode("latin-1"),
    file_name="remito.pdf"
  )