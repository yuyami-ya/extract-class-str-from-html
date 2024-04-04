from typing import Dict, Tuple
import streamlit as st


def show_front_page() -> Tuple[str, Dict]:
    input_html = st.text_area("HTMLを入力")

    if "criteria_list" not in st.session_state:
        st.session_state.criteria_list = [{"tag": "a", "class": "b", "indent": 2}]
    with st.form("form"):
        st_input_area = st.container()
        st_add_button_area = st.container()

        if st_add_button_area.form_submit_button("ADD FORM"):
            st.session_state.criteria_list.append({
                "tag": None,
                "class": None,
                "indent": 0
            })

        if st_add_button_area.form_submit_button("REMOVE FORM"):
            del st.session_state.criteria_list[-1]

        for i in range(len(st.session_state.criteria_list)):
            st_input_area.markdown("---")
            st_input_area.text(f"条件 {i+1}")
            st.session_state.criteria_list[i]["tag"] = st_input_area.text_input("input HTML Tag name", key=i)
            st.session_state.criteria_list[i]["class"] = st_input_area.text_input("input HTML Class name", key=i+100)
            st.session_state.criteria_list[i]["indent"] = st_input_area.selectbox("indent(0~12)", (0,4,8,12), key=i+1000)

        is_pushed = st.form_submit_button("abstract!!!")

        if is_pushed:
            rtn_criteria_list = st.session_state.criteria_list
            is_valid = all(len(_.get("tag")) > 0 and len(_.get("class")) > 0 for _ in rtn_criteria_list)
            if not is_valid:
                st.error("tag or class must NOT be empty!")
            else:
                st.success("Abstracting....")
                st.write(rtn_criteria_list)
                st.session_state.input_html = input_html
        else:
            pass


if __name__ == '__main__':
    show_front_page()