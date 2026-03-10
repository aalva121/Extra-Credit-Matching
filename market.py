import streamlit as st

def initialize_market(num_participants):
    if "market" not in st.session_state:
        st.session_state.market = {
            "num_participants": num_participants,
            "side_A": [],
            "side_B": [],
            "preferences": {}
        }

def add_participant(name, side):
    if side == "A":
        st.session_state.market["side_A"].append(name)
    else:
        st.session_state.market["side_B"].append(name)

def save_preferences(name, ranking):
    st.session_state.market["preferences"][name] = ranking