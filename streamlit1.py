# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:19:31 2025

@author: jignesh
"""
import streamlit as st

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")