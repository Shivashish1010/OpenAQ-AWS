import streamlit as st

from scripts.intro import *
from scripts.cleaning_prepare import *
from scripts.exploratory_analysis import *
from scripts.predict import *
from scripts.results import *
from scripts.visualize import *

st.set_page_config(layout='wide')

from streamlit_option_menu import option_menu

st.sidebar.title("OpenAQ Data Analysis and Prediction")

with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ['Introduction', 'Exploratory Analysis', 'Data cleaning and preparation', 'Visualization','ML/Prediction','Results and Future Works']
    )

if selected == 'Introduction':
    home()
if selected == 'Exploratory Analysis':
    explore()
if selected == 'Data cleaning and preparation':
    cleaner()
if selected ==  'Visualization':
    visualize()
if selected ==  'ML/Prediction':
    predict()
if selected ==  'Results and Future Works':
    result()


