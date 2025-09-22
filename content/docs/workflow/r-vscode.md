+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "在vscode里使用R"
+++

想要在vscode里使用R
在R里面运行install.packages("languageserver")
安装vscode的插件R
现在就能在vscode里用R了，但是非常简陋
建议再进行以下操作
安装radian，pip3 install -U radian（依赖于python，先安装python）
win11在用python3.13安装radian时会报错，需要一些额外的组件，以下版本是没错的
win11-23H2, R-4.3.3, python-3.12.7

运行%USERPROFILE%，新建记事本输入，Sys.setenv(LANG = "en")，重命名为.radian_profile，防止在vscode里出现的中文乱码问题

然后在vscode里配置
"r.bracketedPaste": true,
"r.rpath.windows": "D:\\Program Files\\R\\R-4.3.3\\bin\\R.exe",
"r.rterm.windows": "D:\\Program files\\Python\\Python312\\Scripts\\radian.exe",
"r.rterm.option": [
    "--no-site-file",
],
"r.plot.useHttpgd": true,

以上是最最基本的设置