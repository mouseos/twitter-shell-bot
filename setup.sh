#!/bin/bash
echo "必須パッケージをインストールします。"
sudo apt update
sudo apt install mmdebstrap fakechroot fakeroot
pip3 install tweepy
mkdir rootfs
mmdebstrap --variant=minbase \
 --dpkgopt='path-exclude=/usr/share/man/*' \
 --dpkgopt='path-exclude=/usr/share/locale/*' \
 --dpkgopt='path-exclude=/usr/share/doc/*' \
 --dpkgopt='path-exclude=/var/lib/apt/lists/*debian*' \
 --dpkgopt='path-exclude=/var/cache/apt/*.bin' \
 focal ./rootfs http://jp.archive.ubuntu.com/ubuntu

echo "動作テストします。テスト1成功と表示されれば成功です。"
fakechroot fakeroot chroot rootfs /bin/bash -c "echo \"テスト1成功\" "
python3 commandstart.py "echo \"テスト2成功\" "
