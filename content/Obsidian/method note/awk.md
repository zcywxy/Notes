
相較於 sed 常常作用於一整個行的處理， awk 則比較傾向於一行當中分成數個『欄位』來處理。 因此，awk 相當的適合處理小型的數據資料處理呢！awk 通常運作的模式是這樣的：

## awk 基本格式

```
awk '條件類型1{動作1} 條件類型2{動作2} ...' file
awk '{ awk program }' file
```

file 为 `awk` 要读取的文件，可以是一个或多个文件。如果不指定文件，则从标准输入中读取
awk 可以處理後續接的檔案，也可以讀取來自前個指令的 standard output 。 但如前面說的， awk 主要是處理『每一行的欄位內的資料』，而預設的『欄位的分隔符號為 "空白鍵" 或 "\[tab\]鍵" 』！

```
awk '{ awk program }' a.txt b.txt c.txt
```

**单引号**内的是`awk`的程序，一般使用单引号而非双引号。 `awk`是按行处理文件，内部有一个**隐藏的循环**，即默认下逐行读取文件并运行程序

> 使用单引号原因：双引号中的 $ 会被 shell 解析成 shell 变量引用，于是会进行 shell 变量替换。为了表示`awk`程序使用的变量，所以尽可能使用单引号

## BEGIN 和 END 语句块

```
awk 'BEGIN{print "俺要开始读文件啦"}{print $0}END{print "俺处理完文件啦"}' a.txt
```

-   BEGIN 代码块: 在读取文件前行执行一次，不参与`awk`的隐藏循环
-   END 代码块： 在读取文件完成后执行一次，不参与`awk`的隐藏循环
-   main 代码块：不以`BEGIN`或`END`开头的代码块都称之为 main 代码块， main 代码块会参与 `awk` 的隐藏循环

## awk pattern 和 action

```
awk '
BEGIN {
    n=3
}
/^[0-9]/ {
    print $1
}
END {
    print "end"
}
' a.txt
```

`awk`语法格式为`pattern { action }`模式， 称之为 awk rule

-   pattern 用于筛选符合的文本行
-   action 表示筛选通过后执行的操作
-   pattern 和 action 都可省略
    -   省略 pattern 则不筛选数据，表示对每一行数据都执行 action
    -   省略 {action} 表示对每一行都执行 {print}
    -   省略 action 表示对筛选的行不做任何操作，该语法实际使用中并无意义

可以将 BEGIN 与 END 代码块看成一种特殊的 pattern{action} 代码块

```
# bool pattern
/regular expression/   # 正则匹配，e.g., /a.*ef/{action}
relational expression  # 大小关系匹配，e.g., 3>2{action}
pattern && pattern     # 逻辑与
pattern || pattern     # 逻辑或
!pattern               # 逻辑反
pattern ? pattern : pattern  # 三目运算符

# 范围 pattern
pattern1, pattern2     # 范围匹配，匹配从 pattern1 到 pattern2 之间的内容
```

## `awk` 读取文件

### 记录分隔符

`awk`读取文件时， 每读取一条记录(Record)(默认下按行读取，一行就是一条记录). 每读取一条记录，将其保存到`$0`中，然后执行一次 main 代码段。

可通过修改预定义变量`RS`来改变每次读取的记录模式，`RS`变量表示输入记录分隔符(Record Separator)，默认值为`\n`

`RS`一般设置在 BEGIN 代码块中，因为需要在读取文件前确定好分隔符

> 注：`RS`变量作为输入记录分割符，所读取的每条记录不包含`RS`变量值

-   `RS` 为单个字符， 则直接用该字符来分割记录
-   `RS` 为多个字符，则将其作为正则表达式，只要匹配上正则表达式都用来分割记录
    -   设置预定义变量`IGNORECASE`为非零值，正则匹配时忽略大小写

特殊`RS`值解决特定需求：

```
RS=""    # 按段落读取
RS="^$"  # 一次性读取所有数据, 该正则只能匹配空文件
RS="\n+" # 按行读取，但忽略所有空行
```

`awk`每读取一条记录时，会设置预定义变量`RT`表示记录分割符(Record Termination)。 当`RS`为单个字符时，`RT的值和`RS`值相同。 当`RS`为正则表达式时，`RT\`为正则匹配的记录分隔符
### 行号

`awk`读取每条记录后，将其赋值给`$0`和设置`RT`外，还会设置`NR`和`FNR`这两个预定义变量

-   `NR`: 所有文件的行号计数器
-   `FNR`: 各个文件的行号计数器，针对于多个文件输入的情况

### 字段分割

awk读取每条记录后，将其赋值给0，同时还会对该条记录按照预定义变量FS划分字段，将划分后的各个字段依次存入1，2，3 …，同时将划分好的字段数量赋值给预定义变量NF

```
awk '{print $NF}' a.txt   # 输出 a.txt 的最后一列
```


**awk的环境变量**
$n  当前记录的第n个字段，字段间由FS分隔。
$0   完整的输入记录。
ARGC 命令行参数的数目。
NR 当前记录数。
NF 当前记录中的字段数。
FNR 同NR，但相对于当前文件。
FS 字段分隔符(默认是任何空格)。
RS 记录分隔符(默认是一个换行符)。
OFS 输出字段分隔符(默认值是一个空格)。
ORS 输出记录分隔符(默认值是一个换行符)。

练习
1 删掉第一行和最后一行

```
awk '{print $1}'  | head -n -1 | tail -n+2
```

**head -n -1** - removes last line
**tail -n+2** - starts output from second line (removes 1 line)

awk 'NR>1' filename.csv
awk '{if (NR!=1) {print}}' filename.csv

![[Pasted image 20230125203511.png]]