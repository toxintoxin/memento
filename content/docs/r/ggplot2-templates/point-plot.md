+++
lastmod = 2025-09-17T13:00:00Z
publishDate = 2025-09-12T10:00:00Z
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
