import streamlit as st
import pandas as pd
import plotly.express as px


def visualize():

    st.title('Data Visualization')

    # Yearly representation of total values in 2020 fro India
    df_most = pd.read_csv("./datasets/most_polluting_2020.csv")
    df_most = df_most.query("country == 'India'")
    fig3 = px.bar(df_most, x='city', y=['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'])
    st.write(fig3)

     # Avg Values over most polluting countries in 2019-2020 
    df_2020 = pd.read_csv("./datasets/yearly_polluting_2019-2020.csv")
    fig2 = px.line(df_2020, x='country', y=['PM25_AVG_2019','PM25_AVG_2020'])
    st.write(fig2)

    df = pd.read_csv("./datasets/overall_values_2022.csv",index_col="city")

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

    st.image("./assets/quicksight sheets/sheet-1.png")
    st.markdown("")
    st.image("./assets/quicksight sheets/sheet-2.png")
    st.markdown("")
    st.image("./assets/quicksight sheets/sheet-3.png")
    st.markdown("")
    st.image("./assets/quicksight sheets/sheet-4.png")
    st.markdown("")
    st.image("./assets/quicksight sheets/sheet-5.png")
    st.markdown("")
    st.image("./assets/quicksight sheets/sheet-6.png")
    st.markdown("")

   