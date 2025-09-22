+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "git"
+++

开了vpn, 但git push总是失败443或timeout  
给git设置vpn的端口, v2rayN一般是10809  
```
git config --global http.proxy https://127.0.0.1:10809
git config --global https.proxy https://127.0.0.1:10809
```
