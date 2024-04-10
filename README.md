# HTMLから、特定のクラスの文字を抽出するアプリ

## アプリの説明
  HTML から、特定のclass名のついたタグの文字列を抽出し、リストで返す<br>
  例えば、Udemyの学習する際に、目次を抽出し、印刷することで、ノート代わりに使える。

## 前提条件
 - ブラウザの検証ツール (F12) から、狙ったタグ・クラスを抜き出せる

## 使い方
1. 検証ツールで body タグを コピー、「HTMLを入力」に入力する
1. ほしい文字列の タグ・クラスをコピーし、「条件」にそれぞれ貼り付ける
    1. `ADD Condition` ボタンで、条件を追加できる
    1. `REMOVE Condition` ボタンで、一番最後の条件を削除できる
1. `SAVE` ボタンで、条件を保存する
1. `SHOW` ボタンで、抽出開始
1. 右上からクリップボードへコピーできる


---
# An App for Extracting Text with Specific Classes from HTML

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

## Future Plans
Want to deploy on my own server and automate deployment using Infrastructure as Code (IaC)
