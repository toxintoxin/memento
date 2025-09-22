+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "Ubuntu"
+++

DigitalOcean买的

1vCPU-512MB-10GB, $4/month

Ubuntu 22.04

windows生成SSH密钥
ssh-keygen
建议设置密码

ssh root@ip-addredss

添加用户
sudo useradd -m -s /bin/bash jiayong  
设置密码
sudo passwd jiayong  
添加sudo权限
sudo usermod -aG sudo jiayong
切换到用户jiayong
su - jiayong
复制ssh公钥给jiayong
mkdir -p ~/.ssh
chmod 700 ~/.ssh
sudo cat /root/.ssh/authorized_keys >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys