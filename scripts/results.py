import streamlit as st

def result():
    st.title("Results")

    st.write("We did predictive analysis to get familiar with the data, then cleaned it and filtered it according to our needs. \
    We used previous data to predict the parameters of air quality index and compared it with the actual data to check the accuracy of the model.")
    st.markdown("")

    st.write("We performed descriptive analysis to obtain insights such as daily average values of parameters, concentration of parameters by location and so on. ")
    st.markdown("")

    st.write("After extracting insights from descriptive approach, we performed autoregression on the data collected from past 30 days to predict parameters of the following day as a part of predictive analysis. \
    When we compared the actual and our predicted data, we concluded that we are able to predict data that was close to the actual data.")

    st.markdown("")
    st.title("Future Works")

    st.write("There is one unique thing about OpenAQ data that it is generated in every 10 mins which is almost real time and it is generated from thousands of resources, \
            so in future we are planning to use AWS Kenesis. \
            Using AWS Kinesis, we can visualize data in real time. Performance optimization can be achieved using this technique.")