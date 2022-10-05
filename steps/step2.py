import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

def show_all_products():
  st.info('Lista de precios subida correctamente. Elegí los productos y cantidades debajo para generar el remito!', icon="👇🏻")

  # Retrieve the data from state
  all_products = st.session_state.all_products

  # Create the initial dataframe
  df = pd.DataFrame(all_products, columns=['Cantidad', 'Código', 'Descripción', 'Precio Mayorista', 'Precio final'])

  # AgGrid specific stuff
  gd = GridOptionsBuilder.from_dataframe(df)
  gd.configure_default_column(editable=True, groupable=True)
  gd.configure_selection(selection_mode="multiple", use_checkbox=True)
  gridoptions = gd.build()
  grid_table = AgGrid(
    df,
    gridOptions=gridoptions,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
  )

  # Get the aggrid dictionary
  sel_row = grid_table["selected_rows"]
    
  # Add total price to each product and grand total
  total = 0
  
  for row in sel_row:
    quantity = int(row['Cantidad'])
    productTotal = row["Precio final"] * quantity

    row.update({"Total": productTotal})
    total = total + productTotal
    
  df_sel_row = pd.DataFrame(sel_row)

  # Write the final table
  if not df_sel_row.empty:

    def store_products():
      if 'selected_products' not in st.session_state:
        st.session_state.selected_products = df_sel_row

    st.write("")
    st.write("")
    st.subheader("Productos elegidos:")
    st.dataframe(df_sel_row, use_container_width=True)

    # Write the total and get the button to generate the invoice
    st.metric(label="Total", value="$ {total}".format(total=total))
    st.button('Generar remito', on_click=store_products)

def are_products_selected():
  return 'selected_products' in st.session_state

def reset():
  if 'selected_products' in st.session_state:
    del st.session_state.selected_products