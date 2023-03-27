import numpy
import streamlit as st
import numpy as np

tab1, tab2 = st.tabs(["Tensor", "Zustand"])

with tab1:
    st.header("Tensorprodukt")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Matrix 1")
        rows_ma1 = st.number_input("Anzahl Zeilen M1", step=1)
        columns_ma1 = st.number_input("Anzahl Spalten M1", step=1)
        elements_ma1 = st.text_input("Zeilenweise Elemente M1")
        entries = list(map(float, elements_ma1.split()))
        matrix = np.array(entries).reshape(rows_ma1, columns_ma1)
        st.write(matrix)

    with col2:
        st.header("Matrix 2")
        rows_ma2 = st.number_input("Anzahl Zeilen", step=1)
        columns_ma2 = st.number_input("Anzahl Spalten", step=1)
        elements_ma2 = st.text_input("Zeilenweise Elemente")
        entries_ma2 = list(map(float, elements_ma2.split()))
        matrix_ma2 = np.array(entries_ma2).reshape(rows_ma2, columns_ma2)
        st.write(matrix_ma2)

    with col3:
        def calc_tensor(matrix1, matrix2):
            res_matrix = []
            column = []
            for i in range(len(matrix1)):
                for x in range(len(matrix2)):
                    for y in matrix1[i]:
                        for j in matrix2[x]:
                            erg = j * y
                            column.append(erg)
                    res_matrix.append(column)
                    column = []
            result = np.array(res_matrix)
            return result


        tensor_matrix = calc_tensor(matrix, matrix_ma2)
        st.header("Ergebnis")
        st.write(tensor_matrix)

with tab2:
    st.header("Test")
