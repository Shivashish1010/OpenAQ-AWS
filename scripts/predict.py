import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.tsa.ar_model import AutoReg
import math
import altair as alt

@st.experimental_memo
def load_data():
    df = pd.read_csv("./datasets/april_data.csv")
    df = df.dropna(subset=["location"])

    return df

def load_target_data():
    df = pd.read_csv("./datasets/actual_data.csv")
    df = df.dropna(subset=["location"])

    return df

def predict():
    st.title('Machine Learning/ Prediction')

    df = load_data()
    target_df = load_target_data()

    df = df[df.location.isin(target_df.location)]
    target_df = target_df[target_df.location.isin(df.location)]

    param = st.radio('Choose parameter',['pm25','o3','no2','co','so2','bc','pm10'])
    view_dataset = st.checkbox('View dataset')
    forecasts = {}

    for group, values in df.groupby("location")[param]:
        model = AutoReg(values, lags=0)
        result = model.fit(cov_type="HC0")
        prediction = result.forecast(steps=1)
        forecasts[group] = prediction

    param_pred = pd.DataFrame(forecasts)
    forecasts = {}

    final_df = []
    temp_dict = {}

    for col in param_pred.columns:
        temp_dict['date'] = '2022-04-29'
        temp_dict['location'] = col
        
        for item in param_pred[col]:
            if not math.isnan(item):
                a = item
                temp_dict[param] = item
            
        copy = temp_dict.copy()
        final_df.append(copy)
        temp_dict.clear()

    final_df = pd.DataFrame(final_df)
    final_df = final_df.dropna(subset=[param])
    target_df = target_df.dropna(subset=[param])

    pred_fig = alt.Chart(final_df).mark_line().encode(
        x='location', y=param,color=alt.value('#FF0000')
        )
    target_fig = alt.Chart(target_df).mark_line().encode(
        x='location', y=param,color=alt.value('#0000FF')
        )
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("* Red indicates predicted values")
        with col2:
            st.write("* Blue indicates actual values")
        st.write(pred_fig + target_fig)

    if view_dataset:
        st.write("Predicted dataset")
        st.write(final_df)

