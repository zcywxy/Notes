[[ReadItLater]] [[Article]]

# [Why I love dplyr's across](https://willhipson.netlify.app/post/dplyr_across/dplyr_across/)

Very often I find myself in a situation where I need to perform the same operation on multiple columns in a data set. For this, I turn to none other than `dplyr`’s `across` function. But as we’ll see, not only does `across` help when we are interactively wrangling data, it also operates seamlessly within R functions. Here, I’ll showcase a few simple use cases for `across`.

## How to use `across`

Let’s look at the most basic usage of `across`. For this post I’ll use the **animal crossing items** data set featured on [TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-05-05/readme.md) week 19 of 2020. We get the packages we

```
library(dplyr) # for across and other data wrangling functions
library(readr) # for read_csv

ac_items <- read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/items.csv')

ac_items
```

```
## # A tibble: 4,565 x 16
##    num_id id       name    category orderable sell_value sell_currency buy_value
##     <dbl> <chr>    <chr>   <chr>    <lgl>          <dbl> <chr>             <dbl>
##  1     12 3d-glas… 3D Gla… Accesso… NA               122 bells               490
##  2     14 a-tee    A Tee   Tops     NA               140 bells               560
##  3     17 abstrac… Abstra… Wallpap… TRUE             390 bells              1560
##  4     19 academy… Academ… Dresses  NA               520 bells              2080
##  5     20 acantho… Acanth… Fossils  FALSE           2000 bells                NA
##  6     21 accesso… Access… Furnitu… TRUE             375 bells              1500
##  7     23 acid-wa… Acid-w… Tops     TRUE             420 bells              1680
##  8     24 acid-wa… Acid-w… Bottoms  TRUE             330 bells              1320
##  9     26 acnh-ni… Acnh N… Furnitu… TRUE            8990 bells             35960
## 10     26 acnh-ni… Acnh N… Furnitu… TRUE            8990 bells             35960
## # … with 4,555 more rows, and 8 more variables: buy_currency <chr>,
## #   sources <chr>, customizable <lgl>, recipe <dbl>, recipe_id <chr>,
## #   games_id <chr>, id_full <chr>, image_url <chr>
```

There are two columns related to currency: `sell_value` and `buy_value`. I want to quickly get the mean of these columns for each category. First, here’s how I might do this without `across`:

```
ac_items %>%
  group_by(category) %>%
  summarise(sell_value = mean(sell_value, na.rm = TRUE),
            buy_value = mean(buy_value, na.rm = TRUE))
```

```
## # A tibble: 21 x 3
##    category    sell_value buy_value
##    <chr>            <dbl>     <dbl>
##  1 Accessories       637.     1912.
##  2 Bottoms           298.     1198.
##  3 Bugs             2220.    10511.
##  4 Dresses          1114.     3804.
##  5 Fish             3809.      NaN 
##  6 Flooring         1275.     3833.
##  7 Flowers           121.      160 
##  8 Fossils          3503.      NaN 
##  9 Fruit             125       400 
## 10 Furniture        5387.    20256.
## # … with 11 more rows
```

Which works fine. But imagine if instead of two columns there were 10 or 20 or 100! It would quickly get tedious to add a new line for each column. Here’s where `across` comes in:

```
ac_items %>%
  group_by(category) %>%
  summarise(across(c(sell_value, buy_value), mean, na.rm = TRUE))
```

```
## # A tibble: 21 x 3
##    category    sell_value buy_value
##    <chr>            <dbl>     <dbl>
##  1 Accessories       637.     1912.
##  2 Bottoms           298.     1198.
##  3 Bugs             2220.    10511.
##  4 Dresses          1114.     3804.
##  5 Fish             3809.      NaN 
##  6 Flooring         1275.     3833.
##  7 Flowers           121.      160 
##  8 Fossils          3503.      NaN 
##  9 Fruit             125       400 
## 10 Furniture        5387.    20256.
## # … with 11 more rows
```

Much more efficient. We give `across` a vector of column names followed by the function (in this case `mean`) followed by any other arguments we want to apply to the function.

### Using `~` and `.x`

If we want to provide a *lambda* function, we use what’s called `purrr` syntax. In this example, let’s say we want to divide each price by the maximum price in each category. We’ll use `~` to indicate that we’re supplying a lambda function and use `.x` to indicate where the variable in `across` is used.

```
ac_items %>%
  group_by(category) %>%
  mutate(across(c(sell_value, buy_value), ~ .x / max(.x, na.rm = TRUE),
                .names = "{col}_prop")) %>%
  select(category, ends_with("prop")) # to show new cols
```

```
## # A tibble: 4,565 x 3
## # Groups:   category [21]
##    category    sell_value_prop buy_value_prop
##    <chr>                 <dbl>          <dbl>
##  1 Accessories         0.0113         0.0113 
##  2 Tops                0.035          0.0833 
##  3 Wallpaper           0.00886        0.00886
##  4 Dresses             0.0065         0.0065 
##  5 Fossils             0.333         NA      
##  6 Furniture           0.0015         0.00469
##  7 Tops                0.105          0.25   
##  8 Bottoms             0.307          0.307  
##  9 Furniture           0.0360         0.112  
## 10 Furniture           0.0360         0.112  
## # … with 4,555 more rows
```

## Changing column names

What if we want to change the names of our new columns? We can do this using the `.names` argument.

```
ac_items %>%
  group_by(category) %>%
  summarise(across(c(sell_value, buy_value), mean, na.rm = TRUE, .names = "{col}_mean"))
```

```
## # A tibble: 21 x 3
##    category    sell_value_mean buy_value_mean
##    <chr>                 <dbl>          <dbl>
##  1 Accessories            637.          1912.
##  2 Bottoms                298.          1198.
##  3 Bugs                  2220.         10511.
##  4 Dresses               1114.          3804.
##  5 Fish                  3809.           NaN 
##  6 Flooring              1275.          3833.
##  7 Flowers                121.           160 
##  8 Fossils               3503.           NaN 
##  9 Fruit                  125            400 
## 10 Furniture             5387.         20256.
## # … with 11 more rows
```

`.names` uses `glue` syntax, whereby anything inside the curly braces is a variable. In the case, the name of each column we provide is substituted in `{col}`.

## Multiple functions

What if we want not just the mean, but the standard deviation? `across` can take multiple functions as a list. See here:

```
ac_items %>%
  group_by(category) %>%
  summarise(across(c(sell_value, buy_value),
                   list(mean = mean, sd = sd), na.rm = TRUE, .names = "{col}_{fn}"))
```

```
## # A tibble: 21 x 5
##    category    sell_value_mean sell_value_sd buy_value_mean buy_value_sd
##    <chr>                 <dbl>         <dbl>          <dbl>        <dbl>
##  1 Accessories            637.        1192.           1912.        4384.
##  2 Bottoms                298.         116.           1198.         463.
##  3 Bugs                  2220.        3209.          10511.       14240.
##  4 Dresses               1114.        5247.           3804.       21159.
##  5 Fish                  3809.        4586.            NaN           NA 
##  6 Flooring              1275.        3506.           3833.       10975.
##  7 Flowers                121.         188.            160            0 
##  8 Fossils               3503.        1413.            NaN           NA 
##  9 Fruit                  125           58.4           400            0 
## 10 Furniture             5387.       17604.          20256.       40411.
## # … with 11 more rows
```

## Match column names with `tidyselect`

If we have lots of columns to operate over, it can be cumbersome to spell out each name. We can leverage `tidyselect` helpers to match columns by name or type. Continuing with our example, let’s again calculate the mean sell and buy value by category, but we’ll use `contains` to fetch columns containing *value*.

```
ac_items %>%
  group_by(category) %>%
  summarise(across(contains("value"), mean, na.rm = TRUE, .names = "{col}_"))
```

```
## # A tibble: 21 x 3
##    category    sell_value_ buy_value_
##    <chr>             <dbl>      <dbl>
##  1 Accessories        637.      1912.
##  2 Bottoms            298.      1198.
##  3 Bugs              2220.     10511.
##  4 Dresses           1114.      3804.
##  5 Fish              3809.       NaN 
##  6 Flooring          1275.      3833.
##  7 Flowers            121.       160 
##  8 Fossils           3503.       NaN 
##  9 Fruit              125        400 
## 10 Furniture         5387.     20256.
## # … with 11 more rows
```

Similarly, if we wanted to do this for *any* numeric column in the data, we use `where(is.numeric)`.

```
ac_items %>%
  group_by(category) %>%
  summarise(across(where(is.numeric), mean, na.rm = TRUE, .names = "{col}_"))
```

```
## # A tibble: 21 x 5
##    category    num_id_ sell_value_ buy_value_ recipe_
##    <chr>         <dbl>       <dbl>      <dbl>   <dbl>
##  1 Accessories   3520.        637.      1912.    4.25
##  2 Bottoms       3541.        298.      1198.    7   
##  3 Bugs          3592.       2220.     10511.  NaN   
##  4 Dresses       3583.       1114.      3804.    4.47
##  5 Fish          3024.       3809.       NaN   NaN   
##  6 Flooring      3799.       1275.      3833.    4.41
##  7 Flowers       4946.        121.       160   NaN   
##  8 Fossils       3468.       3503.       NaN   NaN   
##  9 Fruit         2809.        125        400   NaN   
## 10 Furniture     3686.       5387.     20256.    5.01
## # … with 11 more rows
```

## Using `across` programmatically

The above examples highlight why `across` is so useful in day-to-day analytic work flows. But the real reason I love `across` is so it makes programming with `dplyr` so much easier. Here we’re going to quite literally *embrace* `across` - and by ‘embrace’ I mean use `{{}}`.

In this example, we’ll create a function that asks the user to supply any number of numeric columns in their data, and the function will calculate the mean, standard deviation, and 0.05%-95% quantiles. We’ll also allow the user to supply a grouping variable if they want.

```
summarizer <- function(data, numeric_cols = NULL, ...) {
  data %>%
    group_by(...) %>%
    summarise(across({{numeric_cols}}, list(
      mean = ~mean(.x, na.rm = TRUE),
      sd = ~sd(.x, na.rm = TRUE),
      q05 = ~quantile(.x, 0.05, na.rm = TRUE),
      q95 = ~quantile(.x, 0.95, na.rm = TRUE)
    ), .names = "{col}_{fn}"))
}
```

Now we test the function.

```
summarizer(ac_items, numeric_cols = c(sell_value, buy_value),
           category)
```

```
## # A tibble: 21 x 9
##    category    sell_value_mean sell_value_sd sell_value_q05 sell_value_q95
##    <chr>                 <dbl>         <dbl>          <dbl>          <dbl>
##  1 Accessories            637.        1192.            122           2400 
##  2 Bottoms                298.         116.            175            455 
##  3 Bugs                  2220.        3209.            118.         10000 
##  4 Dresses               1114.        5247.            300           1600 
##  5 Fish                  3809.        4586.            180          15000 
##  6 Flooring              1275.        3506.            200           4800 
##  7 Flowers                121.         188.             40            240 
##  8 Fossils               3503.        1413.           1100           5500 
##  9 Fruit                  125           58.4           100            250 
## 10 Furniture             5387.       17604.            130          23775.
## # … with 11 more rows, and 4 more variables: buy_value_mean <dbl>,
## #   buy_value_sd <dbl>, buy_value_q05 <dbl>, buy_value_q95 <dbl>
```

There’s our quick look at `across`. I hope you can appreciate the versatility it offers. Not only does it cut back on typing, but it makes for a more principled approach to data wrangling and can make programming much easier. Also check out `c_across` which is useful for performing an operation that involves multiple columns.