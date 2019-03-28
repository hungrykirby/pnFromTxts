# pnFromTxts
複数のテキストファイルからネガティブ度の遷移を見るプログラム

***

ファイル構成

dictディレクトリを作って、辞書を入れてください。
http://www.lr.pi.titech.ac.jp/~takamura/pubs/pn_ja.dic

txtdataディレクトリに分析したいデータを突っ込んで動かします。

結果はsavedataフォルダー内にoutput.csvとして保存されます。

なお、結果は追記されるので、新しく実行する場合には前のを削除して。

csvの結果は

```
category01, user01, result of 01.txt, result of 02.txt, result of 01.txt
category02, user01, result of 01.txt, result of 02.txt, result of 01.txt
```

みたくなります

```
root/

├ dict/

  └ pn_ja.dic

├ savedata/
 
  └ output.csv

├ txtdata/
  
  ├ category01/

        ├ user01/

            └ 01.txt

            └ 02.txt

            └ 03.txt

        ├ user02/

        └ user03/

  └ category02/

        ├ user01/

        ├ user02/

        └ user03/
```