import copy
from bs4 import BeautifulSoup
import streamlit as st

import front_page

def extract_text_by_criteria(html_str, criteria_list):
    target_class_list = []
    target_tag_list = []
    for criteria_list_elem in criteria_list:
        target_tag_list.append(criteria_list_elem.get("tag"))
        target_class_list.append(criteria_list_elem.get("class"))
    
    soup = BeautifulSoup(html_str, "html.parser")
    elems = soup.find_all(target_tag_list , class_=target_class_list)

    return_text = ""
    for bs_elem in elems:
        bs_elem_tag = bs_elem.name
        bs_elem_class = bs_elem.attrs["class"][0]
        bs_elem_indent = 0
        for c_l_elem in criteria_list:
            c_l_elem_tag = c_l_elem.get("tag")
            c_l_elem_class = c_l_elem.get("class")
            if c_l_elem_tag == bs_elem_tag and c_l_elem_class == bs_elem_class:
                bs_elem_indent = c_l_elem.get("indent")
        soup_elem = BeautifulSoup(str(bs_elem), 'html.parser')
        text = soup_elem.get_text(strip=True)
        output_space = '\u0020' * bs_elem_indent
        return_text += f"{output_space}{text}\n"
    
    return return_text

def main():
    st.markdown('''
        # Extracting Text with Specific Classes from HTML

        ## App Description
        Extracts strings from tags with a specific class name in HTML and returns them as a list. For example, when studying on Udemy, extracting the table of contents and printing it can serve as a substitute for notes.

        ## Prerequisites
        - Able to extract targeted tags and classes using the browser's inspection tool (F12)

        ## How to Use
        1. Copy the body tag using the inspection tool and input it into "Enter HTML"
        1. Copy the desired tag and class for the string and paste them into "Conditions"
            1. Use the `ADD Condition` button to add more conditions
            1. Use the `REMOVE Condition` button to delete the last condition
        1. Use the `SAVE` button to save the conditions
        1. Start extraction by clicking the `SHOW` button
        1. Copy to clipboard from the top right corner
    ''')
    front_page.show_front_page()
    extracted_text = ""
    
    if st.button("SHOW"):
        html_content = copy.deepcopy(st.session_state.input_html)
        criteria = copy.deepcopy(st.session_state.criteria_list)
        extracted_text = extract_text_by_criteria(html_content, criteria)
    
    if extracted_text:
        st.code(extracted_text)

if __name__ == '__main__':
    main()
