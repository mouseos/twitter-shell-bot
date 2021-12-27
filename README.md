# ⚠2021年12月27日11時01分以前のバージョンとフォーク元の利用はAPIキー流出の恐れがあります。
今すぐbotを停止して最新版にしてください。

# twitter-shell-bot

TwitterでUnixコマンドの実行結果を返す簡単なPythonスクリプトです

![test](Docs/test.jpg)
# 動作環境

ubuntu/debianベースOS。（その他の環境では未検証）

# 依存関係

fakeroot,fakechroot,mmdebstrap,python3,tweepy

Debian系OSの場合下記コマンドで依存関係を解決できます。

sudo apt install python3-pip -y && sudo pip3 install tweepy

# 実行する前に

[setup.sh]を実行して必須パッケージをインストールしてください。
chmod +x setup.sh
./setup.sh
[commandstart.py]と[tweet.py]を自身のAPIKeyとTwitterID名に書き換えて使ってください。(TwitterDeveloperに登録している必要があります)
初期状態で記載されているAPIキーはサンプルのため動作しません。

詳細な書き換え項目はコードに記載されています

# 実行の仕方

start.pyを実行するとBotがスタートします。

例:) python3 start.py
