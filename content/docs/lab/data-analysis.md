+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
title = "模型拟合"
+++


prism:

首先要绘制的表格需要是XY类型的
Analyze > XY analyses > Nonlinear regression (curve fit)
然后选择具体的拟合模型
比如随时间增长到平台的y=y0 + A * (1 - exp(-k * time)
Exponential > One phase association

r:
nls()