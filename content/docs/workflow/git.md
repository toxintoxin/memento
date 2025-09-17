+++
lastmod = 2025-09-17T20:00:00+08:00
publishDate = 2025-09-12T18:00:00+08:00
title = "git"
+++

开了vpn, 但git push总是失败443或timeout  
给git设置vpn的端口, v2rayN一般是10809  
```
git config --global http.proxy https://127.0.0.1:10809
git config --global https.proxy https://127.0.0.1:10809
```
