# WaniCTF 2021 spring writeup
Writeup for WaniCTF 2021 spring ( https://score.wanictf.org/#/challenge )
CTFは初めてなので、beginner, easyを中心に解きました。細かめに記録してます。

## Crypto
- Simple Conversion
  - to_bytes()を使って、output.txtに書いてある数字をバイト文字列に変換 (cry-simple-conversion/decrypt.py)
    - ```b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00FLAG{7h1s_i5_h0w_we_c0nvert_m3ss@ges_1nt0_num63rs}'```
    - （最初の方にある\x00の大群は何...？）
- Easy
  - 連立方程式を解いてa,bを求めると、a = 5, b = 8 (cry-easy/decrypt.py)
  - これを使ってdecryptすると、```FLAG{WELCOMETOCRYPTOCHALLENGE}```が得られる
- Can't restore the flag?（途中）
  - 方針：中国剰余定理を使って、探索範囲を狭めると解けそう？
  - 300以下の全ての素数を使って、求める値の一般式を求める
    - 300以下の全ての素数を求める方法：エラトステネスの篩


## Forensics
- presentation
  - パワポのファイルを開いて、青い四角をどかすと ```FLAG{you_know_how_to_edit_ppsx}``` が見えるようになる
- secure document
  - password-generatorに書いてある通りに文字を打ってみると```password: Wan1_20210428_C7F!na!```のようにパスワードが得られる
    - Macユーザなので普段使わないHomeキーなどを知らなかったが、Homeキーで行頭に行く、delキーで右の文字が消去、あたりをエスパーすると行けた
    - AutoHotKeyのスクリプトらしい （[参考](https://miso-24.hatenablog.com/entry/2021/05/02/235918#secure-document)）
  - このパスワードを使ってflag_20210428.zipをunzipすれば、FLAGが書いてあるjpgファイルが解凍される

## misc
- binary
  - 与えられたバイナリを10進数に変換して、さらにlong_to_bytesでバイト文字列に変換　（mis-binary/decrypt.py）
    - ```bits =  38439767368681512622663342949853767042151952614886217293307578660825977289279454932596065360619204221```
    - ```b'FLAG{the_basic_knowledge_of_communication}'```
- Git Master
  - 問題文に載っているリンク先のイメージをpullして、コンテナの生成・起動（[参考](https://qiita.com/k5n/items/2212b87feac5ebc33ecb#%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%92%E7%94%9F%E6%88%90%E3%81%97%E3%81%A6%E8%B5%B7%E5%8B%95%E3%81%99%E3%82%8B)）を行う
  - ```find ./ -name '*.txt' | xargs grep "FLAG"```で、"FLAG"を含むtxtファイルを全文検索
  - すると、```./var/www/html/Flag.txt:FLAG{y0u_```が見つかる（途中で途切れたFLAGが見つかる）
  - 途切れる前の状態がほしいので、問題文で「コミット」とあることも参考にして、コミットログを見てみることに。しかし、/var/www/html/内に.gitがない...
  - 1階層上の、/var/www内に.gitがある！！！
  - gitをインストール（```apt install git-all```）
  - /var/www/のディレクトリで```git log -p -- html/Flag.txt```
    - ログから、```FLAG{y0u__m45t3r}``` が復元できた

## Pwn
- 01 netcat
  - ```nc netcat.pwn.wanictf.org 9001```を叩き、起動したらlsすると、flag.txtが見つかるので、catすると、```FLAG{this_is_the_same_netcat_problem_as_previous_one}```が見つかった
- ✅03
  - まずROP(Return-oriented Programming)とは何かがよくわからなかったのでググる
  - [SECCONのwriteup](https://blog.8f-nai.net/post/2019-01-14-seccon2018/)が参考になる
  - system関数のアドレスを調べる



## Web
- fake
  - リンク先のHTMLを見ると、`<button>`タグ一覧の中に1つだけ`<a>`タグがあるので、hrefに載っているリンク先にアクセスすると、```FLAG{wow_y0u_h4ve_3po4ted_th3_7ake}```が表示されているシークレットページが表示される
- exception
  - hello.pyを見ると、500エラーを起こすとFLAGがresponseの中に入るようになっていることがわかる
  - 意図的に500エラーを起こし、responseを見ると、  ```"flag": "FLAG{b4d_excep7ion_handl1ng}"```が見つかる
    - 意図的に500エラーを起こすのに、まずは普通に適当な名前を送信し、そのときのリクエストをコピー(Copy as fetch)し、nameの値を文字列型ではないものに変えてfetchリクエストを送り直す、という作業を行った



