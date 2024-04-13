from typing import Dict, Tuple
import streamlit as st

def initialize_criteria():
    if "criteria_list" not in st.session_state:
        st.session_state.criteria_list = [{"tag": "a", "class": "b", "indent": 2}]

def add_condition():
    st.session_state.criteria_list.append({"tag": None, "class": None, "indent": 0})

def remove_condition():
    if st.session_state.criteria_list:
        st.session_state.criteria_list.pop()
    else:
        st.error("At least one condition!")

def show_front_page() -> Tuple[str, Dict]:
    input_html = st.text_area("input HTML")
    initialize_criteria()

    with st.form("form"):
        st_input_area = st.container()
        st_add_button_area = st.container()

        if st_add_button_area.form_submit_button("ADD Condition"):
            add_condition()

        if st_add_button_area.form_submit_button("REMOVE Condition"):
            remove_condition()

        for i, criteria in enumerate(st.session_state.criteria_list):
            st_input_area.text(f"Condition {i+1}")
            criteria["tag"] = st_input_area.text_input("input HTML Tag name", key=f"tag_{i}")
            criteria["class"] = st_input_area.text_input("input HTML Class name", key=f"class_{i}")
            criteria["indent"] = st_input_area.selectbox("indent(0~12)", (0,4,8,12), key=f"indent_{i}")
            st_input_area.markdown("---")

        if st.form_submit_button("SAVE"):
            is_valid = all(criteria.get("tag") and criteria.get("class") for criteria in st.session_state.criteria_list)
            if not is_valid:
                st.error("tag or class must NOT be empty!")
            else:
                st.success("success saving condition! push SHOW button.")
                st.session_state.input_html = input_html
                return input_html, st.session_state.criteria_list
