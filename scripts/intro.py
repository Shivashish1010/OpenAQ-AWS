import streamlit as st

def home():
    
    row1_spacer1, row1_1, row1_spacer3 = st.columns(
        (.1, 3, .1)
    )
    row1_1.title('OpenAQ Data Analysis')
    with row1_1:
        st.markdown('Ayushi Mundra, Jay Bhatt, Nehal Kathale, Shivashish Naramdeo')
    st.markdown('')
    st.markdown('')

    row2_spacer1, row2_1, row2_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    row2_1.title('What is OpenAQ?')
    with row2_1:
        st.markdown('OpenAQ is a non-profit organization providing real-time and historical air quality research-grade data.')
        st.markdown('')
        st.markdown('OpenAQ platform is playing a key role in helping understand how air quality is being impacted by hoisting data on Amazon Web Services (AWS)')
        st.markdown('')
        st.markdown('OpenAQ  provides timely access to adequate air quality data.')
        st.markdown('')
        st.markdown('The full historical dataset is publicly accessible via Amazon Simple Storage Service (Amazon S3) buckets.')
        st.markdown('')
        st.markdown('In terms of public health, their work suggests a significant decline in premature deaths and pediatric asthma cases due to the decline in air pollution.')
        st.markdown('')

    row3_spacer1, row3_1, row3_spacer2 = st.columns(
        (.1, 3.2, .1)
    )

    row3_1.title('Business Problem')
    with row3_1:
        st.markdown('Air pollution is a global public health concern that kills more people each year than HIV/AIDS and malaria combined. According to the WHO, one out of every eightdeaths in the world is due to air pollution. Air pollution has various health effects.')
        st.markdown('')

    row4_spacer1, row4_1, row4_spacer2 = st.columns(
        (.1, 3.2, .1)
    )

    row4_1.title('Project Objective')
    with row4_1:
        st.markdown('Descriptive analysis of air pollution index of different countries.')
        st.markdown('')
        st.markdown('How the parameters in the dataset like SO2,CO,NO2 etc. affect different places?')
        st.markdown('')
        st.markdown('Predict air quality parameters based on historical data.')
        st.markdown('')
    