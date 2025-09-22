+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "ggplot2"
+++

## 开头定义变量

```
library(ggplot2)

# 创建一个包含变量的数据框
data <- data.frame(
  x = c(1, 2, 3, 4),
  y = c(10, 20, 30, 40),
  group = c("A", "A", "B", "B")
)

# 定义一个变量，用于替换图形属性
color_var <- "group"

# 使用变量替换创建散点图
ggplot(data, aes(x = x, y = y, color = !!as.name(color_var))) +
  geom_point()
  
ggplot(data, aes(x = x, y = y, color = get(color_var))) +
  geom_point()


ggplot(data, aes(x = x, y = y, color = !!sym(color_var))) +
  geom_point()

ggplot(data, aes(x = x, y = y, color = .data[[color_var]])) +
  geom_point()
```










## export



统一主题

```r
theme_figure <- function(base_size = 7, base_family = "",
                     header_family = NULL,
                     base_line_size = base_size / 22,
                     base_rect_size = base_size / 22,
                     ink = "black", paper = "white", accent = "#3366FF") {
  # Starts with theme_grey and then modify some parts
  theme_grey(
    base_size = base_size,
    base_family = base_family,
    header_family = header_family,
    base_line_size = base_line_size,
    base_rect_size = base_rect_size,
    ink = ink, paper = paper, accent = accent
  ) %+replace%
    theme(

      panel.background = element_rect(fill = "#929292", colour = "#000000"),
      panel.border     = element_rect(colour = "#00FFFF"),

      complete = TRUE
    )
}
```



Cell杂志要求图片中的字为6-8pt，线图的宽度在0.5-1.5pt。  
Science杂志要求图片中字的大小最小为6pt，线图宽度至少为0.5pt。  
综上所述，我们在ggplot2中出图时可以直接设置好字体、字号、颜色和线条宽度等。  

ggplot2中图片格式设置的逻辑很好理解图片

你不需要什么，就把它在theme()中设置为element_blank()即可。

如果需要的话，就根据它的类型（点/线/方框/文字）来指定参数。

- Step1: 设置图片的背景

一般学术论文中的图片都不需要背景，因此设置背景为透明，但给panel添加黑色边框。

设置整个图片的背景为空，这样即可获得透明背景
```
theme(plot.background=element_blank())
```

设置不显示panel的线条，不显示panel的背景，但给panel添加边界，黑色，宽度0.5mm
```
theme(panel.grid=element_blank(),panel.background=element_blank(),panel.border=element_rect(color="black",linewidth=0.5,fill=NA))
#这里设置线的宽度为0.5mm，按理来说0.5mm对应1.415pt，但不知为何，这里的0.5mm粗细的线条在AI中打开后为1.07pt。
```
- Step2: 设置坐标轴和坐标轴刻度线的颜色及粗细

1. 设置横纵坐标轴为空，因为前面已经指定了panel的边框，这里就不需要再加坐标轴了，否则会出现叠加的线条。当然加上也可以，只不过在AI里就会出现多余的线条。（本强迫症当然是不会允许这种事情发生的）
```
theme(axis.line=element_blank())
```

2. 指定坐标轴刻度线为黑色，宽度0.5mm
```
theme(axis.ticks=element_line(color="black",linewidth=0.5))
```
- Step3: 设置文字的字体、字号和颜色

ggplot2中默认所有文字的字体都为Arial，因此无需再指定。而综合CNS杂志的要求，我们建议将字号统一设置为7pt。

1. 指定坐标轴的文字为黑色，字号7pt
```
theme(axis.text=element_text(color="black",size=7))
```

2. 指定坐标轴标题文字为黑色，字号7pt
```
theme(axis.text=element_text(color="black",size=7))
```

3. 指定图片标题为黑色，字号7pt
```
theme(plot.title=element_text(color="black",size=7))
```
- Step4: 对legend进行设置

1. 指定legend的背景设为空
```
theme(legend.background=element_blank(),legend.key=element_blank())
```

2. 指定legend的字号和颜色
```
theme(legend.text=element_text(color="black",size=7),legend.title=element_text(color="black",size=7))
```
将以上所有设置全部写入plot.format变量中，在每次画图时直接添加即可图片
```
plot.format=theme(plot.background=element_blank(),panel.grid=element_blank(),panel.background=element_blank(),panel.border=element_rect(color="black",linewidth=0.5,fill=NA),axis.line=element_blank(),axis.ticks=element_line(color="black",linewidth=0.5),axis.text=element_text(color="black",size=7),axis.title=element_text(color="black",size=7),plot.title=element_text(color="black",size=7),legend.background=element_blank(),legend.key=element_blank(),legend.text=element_text(color="black",size=7),legend.title=element_text(color="black",size=7))

ggplot(data)+geom_boxplot(aes(x=group,y=value,fill=group),outlier.shape=NA)+labs(x="Group",y="Value",title = "Boxplot")+plot.format
```