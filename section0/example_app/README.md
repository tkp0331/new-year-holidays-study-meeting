# what is this section?
Djangoを使って作ったデモ用のアプリを動かしていきます。  
ローカルで作業することを意識したものなのでサーバーでは動きません。あしからず。  
また、動かなかった場合はissue投げて下さい。  

# How to activate and deactivate virtual environment
venvによる仮想環境の上で動くようにしています。  
仮想環境を起動するためには、READMEがある階層から以下のコマンドを実行して下さい。  
```
source ../bin/activate
```
また、仮想環境を停止する際には、以下のコマンドを実行して下さい。  
```
deactivate
```

# How to activate app?

## preparation
まず、SECRET_KEYを準備する必要がありますが、SECRET_KEYをgithubにあげると怒られてしまうのでpushはしていません。  
多分手元で適当に作ることが出来ますが、私は普段`projectname/settings_secret.py`のような機密情報を書くファイルに記載するようにしています。  
このデモアプリでもそのようにしているので、`example_app`フォルダ内に`settings_secret.py`を作って上げる必要があります。  
面倒だと思うので私に連絡してくれれば`settings_secret.py`を送るので教えて下さい。  

## command
仮想環境を起動している状態で,`manage.py`ファイルが存在する階層で以下のコマンドを実行して下さい。  
```
python manage.py runserver
```
`http://128.0.0.1/`的な文章が出てきたら成功です。ちなみにこれは**ループバックアドレス**と言います。覚えておきましょうMyFriends。  
これが出た後、何らかのブラウザ（ある程度何でも大丈夫ですが、Chromeが無難）で検索窓に上のURLをコピペして下さい。  
早まってEnter押しても404エラーなので注意しましょう。  
今回のアプリケーションだったら、エンドポイントは`/hello`または`/world`で指定できるので、`http://128.0.0.1/hello`か`http://128.0.0.1/world`と入力してみて下さい。  
エラーが出ないでそれっぽい画面に遷移したら成功です。  