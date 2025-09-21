+++
lastmod = 2025-09-17T21:00:00+08:00
publishDate = 2025-09-12T18:00:00+08:00
title = "Point plot"
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
