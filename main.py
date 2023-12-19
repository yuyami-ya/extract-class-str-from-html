import datetime
import os
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # -----------------
    # 入力箇所
    criteria_list = [
        {
            "tag": "span",
            "class": "ld-topic-title",
            "indent": 4
        },
        {
            "tag": "div",
            "class": "ld-item-title",
            "indent": 0
        }
    ]
    # -----------------

    path = "./input.html"
    html_str = None
    with open(path) as f:
        html_str = f.read()

    # 入力内容に応じて, find_all()の条件を作成
    target_class_list = []
    target_tag_list = []
    for criteria_list_elem in criteria_list:
        target_tag_list.append(criteria_list_elem.get("tag"))
        target_class_list.append(criteria_list_elem.get("class"))
    
    soup = BeautifulSoup(html_str, "html.parser")
    elems = soup.find_all(target_tag_list , class_=target_class_list)

    ### ファイル出力
    # ファイル名に用いる日付取得
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    # YYYYMMDDhhmmss形式に書式化
    d = now.strftime('%Y%m%d%H%M%S')
    # current dir
    script_dir = os.path.dirname(__file__)
    dir_path = f"{script_dir}/output"
    # TODO(to be fixed): CANNOT mkdirs Linux
    # if directory 'output' doesnt exist, mkdir
    # if not os.path.isdir(dir_path):
    #     print("make output dir")
    #     try:
    #         original_umask = os.umask(0)
    #         os.makedirs(dir_path, mode=755, exist_ok=True)
    #     finally:
    #         os.umask(original_umask)
    #     # os.makedirs(dir_path, mode=0o777, exist_ok=True)
    rel_path = f"output/file_{d}.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, 'w') as f:
        for bs_elem in elems:
            # indent
            bs_elem_tag = bs_elem.name
            bs_elem_class = bs_elem.attrs["class"][0]
            bs_elem_indent = 0
            for c_l_elem in criteria_list:
                c_l_elem_tag = c_l_elem.get("tag")
                c_l_elem_class = c_l_elem.get("class")
                if c_l_elem_tag == bs_elem_tag and c_l_elem_class == bs_elem_class:
                    bs_elem_indent = c_l_elem.get("indent")
            # 
            soup_elem = BeautifulSoup(str(bs_elem), 'html.parser')
            text = soup_elem.get_text(strip=True)
            output_space = '\u0020' * bs_elem_indent
            print(f"{output_space}{text}")
            print(f"{output_space}{text}", file=f)
