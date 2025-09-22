+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title =  "linux"
+++

## 用户管理

### useradd

-D 改变新建用户的预设值
-c 添加备注文字
-d 新用户每次登陆时所使用的家目录
-e 用户终止日期，日期的格式为YYYY-MM-DD
-f 用户过期几日后永久停权。当值为0时用户立即被停权，而值为-1时则关闭此功能，预设值为-1
-g 指定用户对应的用户组
-G 定义附加的用户组
-m 用户目录不存在时则自动创建
-M 不建立用户家目录，优先于/etc/login.defs文件设定
-n 取消建立以用户名称为名的群组
-r 建立系统帐号
-s 登录的shell
-u 指定用户id

### passwd

passwd \<username\>

### groupadd

groupadd \<groupname\>

### usermod

usermod -s /bin/bash \<username\>
usermod -aG \<groupname\> \<username\>

### 查看

cat /etc/passwd
cat /etc/group

### userdel

userdel -r \<username\>     -r是同时删除主目录