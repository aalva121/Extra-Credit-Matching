import streamlit as st

st.title("Matching Market Website")

st.write("Welcome to our ECN 591 Market Design matching platform.")

st.header("Create a Matching Market")

num_participants = st.number_input(
    "Number of participants per side",
    min_value=2,
    max_value=20,
    value=3
)

if st.button("Create Market"):
    st.success(f"Market created with {num_participants} participants per side!")