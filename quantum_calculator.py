import streamlit as st

import numpy as np
import re

def parse_matrix_input(matrix_string):
    """Parses a matrix input string and returns a numpy array"""
    matrix_string = matrix_string.strip()  # remove leading/trailing whitespace
    
    # split input into rows
    rows = matrix_string.split(';')
    if len(rows) == 0:
        return None
    
    # split rows into elements
    matrix = []
    for row in rows:
        elements = row.split()
        if len(elements) == 0:
            return None
        
        # convert elements to strings
        row = [str(element) for element in elements]
        matrix.append(row)
    
    return np.array(matrix)

def calc_tensor(matrix1, matrix2):
            res_matrix = []
            column = []
            for i in range(len(matrix1)):
                for x in range(len(matrix2)):
                    for y in matrix1[i]:
                        for j in matrix2[x]:
                            erg = j + '*' + y
                            column.append(erg)
                    res_matrix.append(column)
                    column = []
            result = np.array(res_matrix)
            return result


tab1, tab2 = st.tabs(["Tensor", "Zustand"])

with tab1:
    st.header("Tensorprodukt")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Matrix 1")
        elements_ma1 = st.text_input("Zeilenweise Elemente M1")
        matrix = parse_matrix_input(elements_ma1)
        st.write(matrix)

    with col2:
        st.header("Matrix 2")
        elements_ma2 = st.text_input("")
        matrix_ma2 = parse_matrix_input(elements_ma2)
        st.write(matrix_ma2)


    tensor_matrix = calc_tensor(matrix, matrix_ma2)
    st.header("Ergebnis")
    st.write(tensor_matrix)

with tab2:
    st.header("Test")
