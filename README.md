# twitter-shell-bot

TwitterでUnixコマンドの実行結果を返す簡単なPythonスクリプトです

![test](Docs/test.jpg)

# 依存関係

python3とtweepyが必要です。

Debian系OSの場合下記コマンドで依存関係を解決できます。

sudo apt install python3-pip -y && sudo pip3 install tweepy

# 実行する前に

[commandstart.py]と[tweet.py]を自身のAPIKeyとTwitterID名に書き換えて使ってください。(TwitterDeveloperに登録している必要があります)


詳細な書き換え項目はコードに記載されています

# 実行の仕方

start.shを実行するとBotがスタートします。

例:) bash start.sh
