import streamlit as st

st.title("Welcome to the MLOps Environment!")
st.write("This is a simple Streamlit application running in your MLOps environment.")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)