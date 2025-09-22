+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "VMware"
+++

## 在A电脑上下载安装vmware

15 pro  
YG5H2-ANZ0H-M8ERY-TXZZZ-YKRV8  

## 安装linux系统

用户名为boss  

## 网络

NAT模式  
映射端口22到10022  
在A电脑上可用ssh boss@localhost -p 10022  
修改A电脑的防火墙设置
入站规则，新建规则，端口，下一步，特定本地端口填10022，下一步，下一步，下一步，名称比如vm ssh port  
新建规则  
其他均默认，端口填10022  
B电脑可用ssh boss@10.10.51.122 -p 10022  