from bs4 import BeautifulSoup

if __name__ == '__main__':
    # -----------------
    # 入力箇所
    input_tag = "div"
    input_class = "curriculum-item-link--curriculum-item-title--2hYub"
    # -----------------

    path = "./input.html"
    html_str = None
    with open(path) as f:
        html_str = f.read()

    target_class = ""
    soup = BeautifulSoup(html_str, "html.parser")
    elems = soup.find_all(input_tag, class_=input_class)
    for elem in elems:
        soup_elem = BeautifulSoup(str(elem), 'html.parser')
        text = soup_elem.get_text(strip=True)
        print(f"{text}")
