import streamlit as st
import pandas as pd
import plotly.express as px
from application_functions import pca_maker

st.set_page_config(layout="wide")
scatter_column, settings_column = st.beta_columns((4, 1))

scatter_column.title("Multi-Dimensional Analysis")

settings_column.title("Settings")

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    data_import = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols = pca_maker(data_import)

    categorical_variable = settings_column.selectbox("Variable Select", options = cat_cols)
    categorical_variable_2 = settings_column.selectbox("Second Variable Select", options = cat_cols)

    pca_1 = settings_column.selectbox("First Principle Component", options=pca_cols, index=0)
    pca_cols.remove(pca_1)
    pca_2 = settings_column.selectbox("Second Principle Component", options=pca_cols)

    

    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2, color=categorical_variable, template="simple_white", height=800, hover_data = [categorical_variable_2]), use_container_width=True)

else:
    scatter_column.header("Please Choose a file")

