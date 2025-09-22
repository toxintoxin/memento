+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "CellRanger"
+++

2024年4月2日，最新版本为8.0.0  
接下来的内容以此为例  

## 安装

### 下载

需要在10x官网注册账号后即可看到下载链接  

```
mkdir software
cd software
```

```
wget -O cellranger-8.0.0.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-8.0.0.tar.gz?Expires=1712160958&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA&Signature=DQW0qM6u2Ju-GUf-DCIlGuKa0A~lH1O7aaFrtaNJXfEFYI~36hNf-7a2GcZQtnpHbS~Ai5vUSurF26Ppr5taJAVFgK7I0BHOkYiJqBjtOfoPhtMEMayRFRDc~bjqnicC1RLPPrBRVLPfRJe0F7RMd4Srgm7t3HhcMzT-y-Y3vLRUx7Z8vHw-NFWqhJSN84Rwf9t3mDS3odJv5CL9hAjzYsSWYzjTyjjvkJ0MWnzvhryIzVT5~fDmZJWjLdCKfU~DSt6c7cp-K1uHFe~slfEQgtvwpDIF6oyRLHZSNNVKFNgSZ4af1iziyW-E2Vkc~Ax0SlBBW10RTZspF3U~7x6YEw__"
```

### 解压

```
tar -zxvf cellranger-8.0.0.tar.gz
```

### 添加环境变量

```
echo 'export PATH=/home/user_name/software/cellranger-8.0.0:$PATH' >> ~/.bashrc
source  ~/.bashrc
```

### 测试

```
cellranger -V
```

## 使用

```
cellranger -V
```
