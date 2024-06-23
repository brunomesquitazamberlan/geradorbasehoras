import streamlit as st
import pandas as pd
import io

def transforma_csv(input_df):
    # Função de exemplo que transforma o DataFrame de entrada
    input_dataframe = pd.read_csv(input_df)
    
    df1 = input_dataframe.copy()
    df2 = input_dataframe.copy()
    
    # Exemplos de transformações
    return df1, df2

def main():
    st.title("Upload de CSV e Download dos Resultados Transformados")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        
        result = transforma_csv(uploaded_file)

        # Convertendo DataFrames para CSV
        csv1 = result[0].to_csv(index=False).encode('utf-8')
        csv2 = result[1].to_csv(index=False).encode('utf-8')


        st.download_button(
            label="Baixar primeiro CSV",
            data=csv1,
            file_name='transformado1.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Baixar segundo CSV",
            data=csv2,
            file_name='transformado2.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()
