# アプリの説明
  HTML から、特定のclass名のついたタグの文字列を抽出し、リストで返す  
  Webページでは、カード形式や、リスト形式で、タイトルが並んでることがある。  
  その同じ形式で並んでるタイトル等を、一覧で抜き出すツール

# 前提条件
 - エディタを使える(VScode等)
 - pipenv がインストールされてる
   `pip install pipenv` （[pipenvについて]）(https://zenn.dev/nekoallergy/articles/py-env-pipenv01)
 - 検証ツールから、ほしい文字列のタグ・クラスを抜き出せる

# 使い方
1. 検証ツールで body タグをcopy し、 input.html に貼り付ける. 
1. 抜き出す対象のclass をコピペ  
    複数クラスついてれば、全て抜き出す  
  `main.py` の入力箇所に、`HTMLタグ`、`class`をそれぞれ入力する

1. `pipenv install`
1. `pipenv run start`
1. ターミナルに一覧で出力される
