+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "把shiny应用作为R包开发"
+++

## 创建一个新的R包

使用`usethis`包来快速创建一个新的R包结构。
```
# 安装usethis包（如果尚未安装）
install.packages("usethis")

# 创建一个新的R包
usethis::create_package("myApp")
```
这将在当前工作目录中创建一个名为myApp的文件夹，其中包含一个基本的R包结构，`DESCRIPTION`，`NAMESPACE`，`/R`。创建完成后工作目录会自动切换到myApp

`DESCRIPTION`里面的Imports声明了依赖的包，会在安装myApp的时候检查尚未安装的依赖包

`NAMESPACE`里面包含了myApp所用的包或具体函数, 以及产生的函数。 若在某个模块里用了ggplot2的函数, 就需要在`NAMESPACE`里面`import(ggplot2)`, 并非手动编辑, 通过在模块的.R文件里写注释, 然后用`devtools::document()`自动更新`NAMESPACE`

## 添加Shiny应用程序代码

在R包中添加shiny应用程序的代码。通常，shiny应用程序的代码可以放在inst/app目录下。
```
# 创建inst/app目录
usethis::use_directory("inst/app")

# 在inst/app目录下创建一个app.R文件
file.create("inst/app/app.R")
```





## 常用函数

```
# 加载当前工作目录下的包
devtools::load_all()
```

```
# 更新DESCRIPTION文件
usethis::use_package("packagename")
```

```
# 更新NAMESPACE文件
devtools::document()
```

```
# deploy to shinyapps.io

```

```
# 从github安装R包
remotes::install_github("username/repository")
```