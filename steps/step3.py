import streamlit as st

def show_form():
  st.write('')

  # Invoice form
  with st.form("invoice_form"):
    st.subheader("Datos para el remito")

    col1, col2 = st.columns(2)

    with col1:
      invoices = st.text_area("Números de las facturas", placeholder="Ejemplo: \n00000001, 00000002, 00000003, etc.")
      transport = st.text_input("Información del transportista", placeholder="Completá acá la información de quien hace el envío")
    
    with col2:
      recipient = st.text_area("Información del destinatario", placeholder="Completá acá la información de quien recibe")
      phone = st.text_input("Teléfono", placeholder="Completá el teléfono del transportista acá")
      
    insurance = st.number_input("Valor del seguro", min_value=0, value=0, step=100)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Generar")
    if submitted:
      if 'invoice_information' not in st.session_state:
        st.session_state.invoice_information = [invoices, transport, recipient, phone, insurance]

def is_form_submitted():
  return 'invoice_information' in st.session_state

def reset():
  if 'invoice_information' in st.session_state:
    del st.session_state.invoice_information