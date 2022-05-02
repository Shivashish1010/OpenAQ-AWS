import pandas as pd
import plotly.express as px
import streamlit as st
from statsmodels.tsa.ar_model import AutoReg
import math
import altair as alt

@st.experimental_memo
def load_data():
    df = pd.read_csv("sample-data.csv")
    df = df.dropna(subset=["location"])

    return df

def load_target_data():
    df = pd.read_csv("target-data.csv")
    df = df.dropna(subset=["location"])

    return df


st.sidebar.title("OpenAQ Data Analysis and Prdiction")
st.sidebar.write("Choose the following:")

btn1 = st.sidebar.button("OpenAQ data analysis and visualization")
btn2 = st.sidebar.button("OpenAQ Prediction")

if not btn2:
    df = pd.read_csv("overall_values_2022.csv",index_col="city")

    df.loc[df.value < 0, 'value'] = 0
    df['year'] = pd.to_datetime(df['utc_date'])
    df["year"] = df["year"].dt.year
    daily_df = df.groupby(
        ['parameter','year']
    )['value'].mean().reset_index(name='Overall Average')

    #Overall Average of parameter over the world in 2022
    fig = px.line(daily_df,          
        x="parameter",         
        y="Overall Average",   
        title=f"Overall Average of parameter",
        labels={"parameter": "# parameter","value": "Overall Average"},
        color='year',
        height=500,
        width=800)
    st.write(fig)


    # Mean Values of all parameters in US from 2021-2022 April
    df1 = pd.DataFrame(df,columns=["country","utc_date","parameter","value","location"])
    mask = (df['utc_date'] > '2021-03-29')
    df1 = df1.loc[mask]


    df1 = df1.groupby(["country","utc_date","location"])
    df1 = df1["value"].mean().reset_index()
    df1 = df1.sort_values(by=["value"])
    df1['value'] = pd.to_numeric(df1['value'])
    df1 = df1.loc[df1['value'] > 6]

    fig1 = px.line(df1, x='utc_date', y='value',color="country")
    st.write(fig1)

    # Avg Values over most polluting countries in 2019-2020 
    df_2020 = pd.read_csv("yearly_polluting_2019-2020.csv")
    fig2 = px.line(df_2020, x='country', y=['PM25_AVG_2019','PM25_AVG_2020'])
    st.write(fig2)

    # Yearly representation of total values in 2020 fro India
    df_most = pd.read_csv("most_polluting_2020.csv")
    df_most = df_most.query("country == 'India'")
    fig3 = px.bar(df_most, x='city', y=['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    st.write(fig3)
else:
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
        a=0
        b=0
        
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





