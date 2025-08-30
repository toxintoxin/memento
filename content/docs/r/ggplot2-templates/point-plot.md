+++
lastmod = 2024-07-26
title = "point-plot"
+++


```r
library(dplyr)
```

```r
library(ggplot2)
```

```r
iris %>%
    ggplot(aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
    geom_point(size = 1, alpha = 0.7) +
    labs(
        title = "Sepal Length vs Sepal Width",
        x = "Sepal Length (cm)",
        y = "Sepal Width (cm)",
        color = "Species"
    )
```
