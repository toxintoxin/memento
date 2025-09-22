+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "启动项目"
+++

技术栈

前端: React (Next.js) + TailwindCSS  
后端: FastAPI + MongoDB  
桌面端封装: Tauri  
自动更新: GitHub Releases

## Date

2025-03-16

## Prerequisites


### System

ubuntu 22.04

### Rust

```
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

### Node.js

```
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 22

# Verify the Node.js version:
node -v # Should print "v22.14.0".
nvm current # Should print "v22.14.0".

# Verify npm version:
npm -v # Should print "10.9.2".
```

rust 1.85.1


## Create a project

```
# 官方推荐的Bash会报错
sh <(curl https://create.tauri.app/sh)
```