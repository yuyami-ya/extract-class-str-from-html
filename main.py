import datetime
import os
import copy
from bs4 import BeautifulSoup
import streamlit as st

import front_page

def abstruct_from_html():
    html_str = copy.deepcopy(st.session_state.input_html)
    criteria_list = copy.deepcopy(st.session_state.criteria_list)

    target_class_list = []
    target_tag_list = []
    for criteria_list_elem in criteria_list:
        target_tag_list.append(criteria_list_elem.get("tag"))
        target_class_list.append(criteria_list_elem.get("class"))
    
    soup = BeautifulSoup(html_str, "html.parser")
    elems = soup.find_all(target_tag_list , class_=target_class_list)

    # TODO: txtファイルに出力し, ダウンロードできるようにする.
    # ### ファイル出力
    # # ファイル名に用いる日付取得
    # t_delta = datetime.timedelta(hours=9)
    # JST = datetime.timezone(t_delta, 'JST')
    # now = datetime.datetime.now(JST)
    # # YYYYMMDDhhmmss形式に書式化
    # d = now.strftime('%Y%m%d%H%M%S')
    # # current dir
    # script_dir = os.path.dirname(__file__)
    # dir_path = f"{script_dir}/output"
    # rel_path = f"output/file_{d}.txt"
    # abs_file_path = os.path.join(script_dir, rel_path)

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
        print(f"{output_space}{text}")
        return_text += f"{output_space}{text}\n"
    
    return return_text


def main():
    return_text = None
    front_page.show_front_page()
    if st.button("Show"):
        return_text = abstruct_from_html()
    if return_text:
        st.code(return_text)


if __name__ == '__main__':
    main()